import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="WeatherVision-AI", layout="wide")

# CSS Terpadu
st.markdown("""
<style>
    /* 1. Background Aplikasi */
    .stApp { background-color: #fdba74 !important; }
    
    /* 2. Sembunyikan Header hanya di PC (menjaga agar tombol menu di HP tidak hilang) */
    @media (min-width: 768px) {
        #MainMenu, header { visibility: hidden; }
    }

    /* 3. Sidebar Cokelat */
    [data-testid="stSidebar"] { 
        background-color: #78350f !important; 
        padding-top: 2rem;
    }
    [data-testid="stSidebar"] a, [data-testid="stSidebar"] span { 
        color: #ffffff !important; 
        font-weight: 500;
        font-size: 1.1rem;
    }

    /* 4. Banner Header */
    .header-banner {
        background-color: #9a3412 !important; 
        border-radius: 12px;
        border: 4px solid #7c2d12 !important; 
        padding: 25px;
        text-align: center;
        margin-bottom: 25px;
        width: 100%;
    }
    .header-banner h1 { color: #ffffff !important; font-weight: 800 !important; margin: 0; font-size: 2.5em; }
    .header-banner p { color: #ffffff !important; font-size: 1.2rem; opacity: 0.9; margin-top: 5px; }

    /* 5. Kartu Fitur - Memastikan tinggi seragam */
    [data-testid="column"] {
        display: flex;
    }
    .feature-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 3px solid #c2410c !important;
        text-align: center;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        min-height: 200px; /* Menambah tinggi minimum agar seragam */
    }
</style>
""", unsafe_allow_html=True)

# Banner
st.markdown("""
<div class='header-banner'>
    <h1>📖 WEATHERVISION-AI</h1>
    <p>Sistem Cerdas Pemantauan Cuaca Real-Time</p>
</div>
""", unsafe_allow_html=True)

# Grid Layout untuk 4 Menu
st.markdown("<h2 style='text-align: center; color: #78350f; margin-bottom: 30px;'>Menu Utama</h2>", unsafe_allow_html=True)

# Menggunakan 2 kolom
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class='feature-card'>
        <h3>ℹ️ About</h3>
        <p>Informasi mengenai visi, teknologi, dan tim di balik WeatherVision-AI.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='feature-card'>
        <h3>📊 Dashboard</h3>
        <p>Pantau data cuaca terkini, grafik suhu, dan statistik hasil deteksi.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-card'>
        <h3>📷 Scan Cuaca</h3>
        <p>Unggah foto kondisi cuaca, dan biarkan AI kami mengidentifikasi kondisi cuaca secara akurat.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='feature-card'>
        <h3>📜 History</h3>
        <p>Tinjau kembali riwayat hasil deteksi cuaca Anda untuk melihat tren perubahan.</p>
    </div>
    """, unsafe_allow_html=True)