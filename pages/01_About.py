import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="About - WEATHERVISION-AI",
    layout="wide",
    initial_sidebar_state="expanded"  # Sidebar tetap terbuka
)

# =========================
# CSS CUSTOM
# =========================
st.markdown("""
<style>

/* =========================
   SIDEBAR STREAMLIT
========================= */

/* Warna sidebar */
[data-testid="stSidebar"] {
    background-color: #A0522D;
}

/* Warna text sidebar */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Tombol hamburger HP */
button[kind="header"] {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 10px !important;
    left: 10px !important;
    z-index: 999999 !important;
    background-color: #9a3412 !important;
    border-radius: 10px !important;
    padding: 6px 10px !important;
}

/* Paksa sidebar tetap muncul di HP */
@media (max-width: 768px) {

    [data-testid="stSidebar"] {
        transform: translateX(0%) !important;
        visibility: visible !important;
    }

    section[data-testid="stSidebar"] {
        display: block !important;
    }
}

/* =========================
   GLOBAL APP
========================= */

.stApp {
    background-color: #fdba74 !important;
}

#MainMenu,
footer {
    visibility: hidden;
}

/* =========================
   HEADER BANNER
========================= */

.header-banner {
    background-color: #9a3412 !important;
    border-radius: 12px;
    border: 4px solid #7c2d12 !important;
    padding: 25px;
    text-align: center;
    margin-bottom: 25px;
    width: 100%;
}

.header-banner h1 {
    color: #ffffff !important;
    font-weight: 800 !important;
    margin: 0;
    font-size: 2.5em;
}

.header-banner h2 {
    color: #ffffff !important;
    font-weight: 500 !important;
    margin: 5px 0 0 0;
    font-size: 1.5em;
    opacity: 0.9;
}

/* =========================
   CONTENT CARD
========================= */

.content-card {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 15px;
    border: 3px solid #c2410c !important;
    margin-bottom: 20px;
}

.section-title {
    color: #9a3412;
    font-weight: 800;
    font-size: 1.5em;
    margin-bottom: 15px;
}

/* =========================
   RESPONSIVE MOBILE
========================= */

@media (max-width: 768px) {

    .header-banner h1 {
        font-size: 1.8em !important;
    }

    .header-banner h2 {
        font-size: 1em !important;
    }

    .content-card {
        padding: 20px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# UI HEADER
# =========================
st.markdown("""
<div class='header-banner'>
    <h1>📖WEATHERVISION-AI</h1>
    <h2>Tentang Kami</h2>
</div>
""", unsafe_allow_html=True)

# =========================
# CONTENT
# =========================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class='content-card'>
        <div class='section-title'>🚀 Visi Kami</div>
        <p>
        WEATHERVISION-AI hadir untuk menjembatani teknologi kecerdasan buatan 
        dengan pemantauan lingkungan. Kami berkomitmen memberikan data cuaca 
        yang akurat, cepat, dan mudah diakses melalui teknologi computer vision.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='content-card'>
        <div class='section-title'>🛠️ Core Capabilities</div>
        <ul>
            <li><b>Deteksi Cuaca Real-time:</b> Klasifikasi kondisi cuaca secara instan.</li>
            <li><b>Prediksi Suhu Presisi:</b> Estimasi suhu berbasis analisis sensor.</li>
            <li><b>Analisis Visual:</b> Memproses gambar untuk wawasan cuaca mendalam.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# =========================
# TECH STACK
# =========================
# =========================
# TECH STACK
# =========================
st.markdown("""
<div class="content-card" style="text-align:center;">

<h2 class="section-title">⚙️ Teknologi Pendukung</h2>

<p>
Aplikasi ini dibangun menggunakan ekosistem teknologi modern
untuk performa maksimal.
</p>

<div style="
display:flex;
justify-content:center;
gap:20px;
flex-wrap:wrap;
margin-top:20px;
">

<div style="
padding:12px 25px;
background:#fffaf6;
border-radius:10px;
border:1px solid #c2410c;
font-weight:bold;
">
🐍 Python
</div>

<div style="
padding:12px 25px;
background:#fffaf6;
border-radius:10px;
border:1px solid #c2410c;
font-weight:bold;
">
📊 Streamlit
</div>

<div style="
padding:12px 25px;
background:#fffaf6;
border-radius:10px;
border:1px solid #c2410c;
font-weight:bold;
">
🤖 RoboFlow
</div>

</div>

</div>
""", unsafe_allow_html=True)
# =========================
# FOOTER NAVIGASI
# =========================
if st.button("⬅️ Kembali ke Home"):
    st.switch_page("app.py")