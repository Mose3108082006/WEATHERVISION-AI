import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    layout="wide",
    page_title="AI Cuaca Detector",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS CUSTOM
# ==========================================
st.markdown("""
<style>

/* ==========================================
   SIDEBAR
========================================== */

[data-testid="stSidebar"] {
    background-color: #A0522D;
    padding-top: 20px;
}

/* Warna text sidebar */
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Sidebar tetap bisa dibuka di HP */
@media (max-width: 768px) {

    section[data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
    }

    [data-testid="collapsedControl"] {
        display: block !important;
        visibility: visible !important;
    }
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

/* ==========================================
   GLOBAL APP
========================================== */

.stApp {
    background-color: #fdba74 !important;
}

/* JANGAN sembunyikan header */
#MainMenu,
footer {
    visibility: hidden;
}

/* ==========================================
   RADIO SIDEBAR
========================================== */

div[role="radiogroup"] > label {
    display: none !important;
}

div[role="radiogroup"] {
    gap: 0px !important;
}

[data-testid="stSidebar"] .stRadio > div > label {
    font-weight: 500;
    font-size: 18px;
    color: #374151;
    padding: 5px 10px;
}

/* ==========================================
   HEADER
========================================== */

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

/* ==========================================
   METRIC CARD
========================================== */

.metric-card {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 10px;
    border: 3px solid #c2410c !important;
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

/* ==========================================
   EXPANDER
========================================== */

.stExpander {
    border: 2px solid #9a3412 !important;
    border-radius: 12px !important;
    background-color: #fffaf6 !important;
}

/* ==========================================
   RESPONSIVE MOBILE
========================================== */

@media (max-width: 768px) {

    .header-banner h1 {
        font-size: 1.8em !important;
    }

    .metric-card {
        margin-bottom: 10px;
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGASI
# ==========================================
with st.sidebar:
    page = st.radio(
        " ",
        ["app", "about", "history", "home", "scan"],
        index=3
    )

# ==========================================
# HEADER DASHBOARD
# ==========================================
st.markdown("""
<div class='header-banner'>
    <h1>🏠WEATHERVISION-AI</h1>
    <p>Dashboard Cuaca terkini</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# BARIS STATISTIK
# ==========================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-label'>Cuaca Terakhir</div>
        <div class='metric-value'>Cerah ☀️</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-label'>Suhu Rerata</div>
        <div class='metric-value'>30.5°C</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-label'>Total Scan</div>
        <div class='metric-value'>141</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# GRAFIK
# ==========================================
st.write("")

st.subheader("📊 Tren Suhu 7 Hari Terakhir")

chart_data = pd.DataFrame(
    np.random.randn(7, 1),
    columns=['Suhu (°C)']
)

st.line_chart(chart_data)

# ==========================================
# PANDUAN PENGGUNAAN
# ==========================================
st.write("")

with st.expander(
    "📖 Klik di sini untuk Panduan Penggunaan Aplikasi",
    expanded=False
):

    st.markdown(
        "<h4 style='color: #9a3412;'>Panduan Operasional & Sistem</h4>",
        unsafe_allow_html=True
    )

    col_a, col_b = st.columns(2)

    with col_a:

        st.markdown("### 🛠️ Langkah Operasional")

        st.markdown("""
        * **Scan Data:** Klik menu `scan`
        untuk memicu pemindaian sensor.

        * **Monitoring:** Kembali ke `home`
        untuk melihat data real-time.

        * **Analisis:** Buka `history`
        untuk melihat tren data historis.
        """)

    with col_b:

        st.markdown("### 🛡️ Catatan Sistem")

        st.markdown("""
        * **Koneksi:** Pastikan modul sensor
        terhubung ke jaringan aktif.

        * **Update:** Data diperbarui
        secara otomatis setiap 5 menit.

        * **Bantuan:** Jika sistem error,
        tekan tombol Refresh browser.
        """)

    st.info(
        "💡 Tips: Pastikan sensor cuaca "
        "berada di area terbuka untuk "
        "hasil yang akurat."
    )
