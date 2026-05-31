import streamlit as st
import time

from services.roboflow_service import predict_weather
from services.temperature_service import predict_temperature
from services.history_service import save_history

# ==========================================
# CONFIG & SETTING TATA LETAK WIDE
# ==========================================
st.set_page_config(
    layout="wide",
    page_title="AI Cuaca Detector",
    initial_sidebar_state="expanded"
)

# ==========================================
# SIDEBAR COLOR
# ==========================================
st.markdown("""
<style>

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #A0522D;
}

/* Text sidebar */
[data-testid="stSidebar"] a,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Tombol hamburger HP */
button[kind="header"] {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999999 !important;
    background-color: #9a3412 !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Sidebar mobile */
@media (max-width: 768px) {

    [data-testid="collapsedControl"] {
        display: block !important;
        visibility: visible !important;
    }

    section[data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# INJEKSI CSS - DESAIN MINIMALIS & BERSIH
# ==========================================
st.markdown("""
<style>

/* Background utama */
.stApp {
    background-color: #fdba74 !important;
}

/* JANGAN sembunyikan header */
#MainMenu,
footer {
    visibility: hidden;
}

/* Banner */
.header-banner {
    background-color: #9a3412 !important;
    border-radius: 12px;
    border: 4px solid #7c2d12 !important;
    padding: 25px;
    text-align: center;
    margin-bottom: 25px;
}

.header-banner h1,
.header-banner p {
    color: #ffffff !important;
    font-weight: 800 !important;
}

/* Container utama hasil */
div[data-testid="stColumn"] {
    background-color: #ffffff !important;
    border-radius: 12px !important;
    border: 3px solid #c2410c !important;
    padding: 20px !important;
}

/* Kartu Statistik */
.metric-card {
    background-color: #fffaf6;
    padding: 15px;
    border-radius: 10px;
    border: 2px solid #9a3412;
    text-align: center;
    margin: 5px;
}

.metric-label {
    color: #9a3412;
    font-weight: 600;
    font-size: 0.9em;
    text-transform: uppercase;
}

.metric-value {
    font-size: 1.4em;
    font-weight: 800;
    color: #000000;
    margin-top: 5px;
}

/* Responsive HP */
@media (max-width: 768px) {

    .header-banner h1 {
        font-size: 1.7em !important;
    }

    .header-banner p {
        font-size: 0.9em !important;
    }

    div[data-testid="stColumn"] {
        padding: 15px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# BANNER JUDUL
# ==========================================
st.markdown("""
<div class="header-banner">
    <h1>📷WEATHERVISION-AI</h1>
    <p>Upload atau ambil foto untuk prediksi cuaca instan</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# LOGIKA APLIKASI
# ==========================================
if "open_camera" not in st.session_state:
    st.session_state["open_camera"] = False

col1, col2 = st.columns([1, 1.5])

# ==========================================
# UPLOAD
# ==========================================
with col1:

    st.markdown("### 📁 Upload Gambar")

    uploaded_image = st.file_uploader(
        "Pilih file",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

if uploaded_image:
    st.session_state["open_camera"] = False

# ==========================================
# CAMERA
# ==========================================
with col2:

    st.markdown("### 📷 Kamera Langsung")

    btn_text = (
        "❌ Tutup Kamera"
        if st.session_state["open_camera"]
        else "Aktifkan Kamera"
    )

    if st.button(btn_text):
        st.session_state["open_camera"] = (
            not st.session_state["open_camera"]
        )

if st.session_state["open_camera"]:
    camera_image = st.camera_input("Ambil Foto")
else:
    camera_image = None

# ==========================================
# PILIH GAMBAR
# ==========================================
selected_image = (
    uploaded_image
    if uploaded_image
    else camera_image
)

# ==========================================
# HASIL ANALISIS
# ==========================================
if selected_image:

    st.write("---")

    col_preview, col_hasil = st.columns(2)

    # Preview
    with col_preview:

        st.markdown("### 🖼️ Preview")

        st.image(
            selected_image,
            use_container_width=True
        )

        trigger_analisis = st.button(
            "Analisis AI",
            use_container_width=True
        )

    # Hasil
    with col_hasil:

        st.markdown("### 🌤️ Hasil Analisis AI")

        if trigger_analisis:

            with st.spinner(
                "AI sedang menganalisis..."
            ):

                result = predict_weather(
                    selected_image
                )

            if not result["valid"]:

                st.error(
                    f"❌ {result['reason']}"
                )

            else:

                weather = result["weather"]

                temp_data = predict_temperature(
                    weather
                )

                # Header hasil
                c1, c2 = st.columns(2)

                c1.metric(
                    "Cuaca",
                    weather.capitalize()
                )

                c2.metric(
                    "Confidence",
                    f"{result['confidence']}%"
                )

                st.write("---")

                st.markdown(
                    "#### Detail Statistik Suhu:"
                )

                # Statistik 1
                r1_c1, r1_c2 = st.columns(2)

                r1_c1.markdown(
                    f"""
                    <div class='metric-card'>
                        <div class='metric-label'>
                            Rerata
                        </div>
                        <div class='metric-value'>
                            {temp_data['tavg']}°C
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                r1_c2.markdown(
                    f"""
                    <div class='metric-card'>
                        <div class='metric-label'>
                            Min
                        </div>
                        <div class='metric-value'>
                            {temp_data['tmin']}°C
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Statistik 2
                r2_c1, r2_c2 = st.columns(2)

                r2_c1.markdown(
                    f"""
                    <div class='metric-card'>
                        <div class='metric-label'>
                            Maks
                        </div>
                        <div class='metric-value'>
                            {temp_data['tmax']}°C
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                r2_c2.markdown(
                    f"""
                    <div class='metric-card'>
                        <div class='metric-label'>
                            Hujan
                        </div>
                        <div class='metric-value'>
                            {temp_data['prcp']} mm
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Simpan histori
                save_history({
                    "weather": weather,
                    "temperature": temp_data['suhu_prediksi'],
                    "confidence": result['confidence']
                })

