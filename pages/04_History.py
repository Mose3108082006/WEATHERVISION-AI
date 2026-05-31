import streamlit as st
import json
import os

# Pastikan set_page_config ada di setiap file pages
st.set_page_config(page_title="WEATHERVISION-AI", layout="wide")

st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #A0522D; }
    [data-testid="stSidebar"] a, [data-testid="stSidebar"] span { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .stApp { background-color: #fdba74 !important; }
    #MainMenu, header { visibility: hidden; }

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
    .header-banner h2 { color: #ffffff !important; font-weight: 500 !important; margin: 5px 0 0 0; font-size: 1.5em; opacity: 0.9; }
    
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #c2410c !important;
        margin: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- UI HEADER ---
st.markdown("""
<div class='header-banner'>
    <h1>📖 WEATHERVISION-AI</h1>
    <h2>Riwayat Pemindaian</h2>
</div>
""", unsafe_allow_html=True)

# --- LOGIKA DATA ---
file_path = "storage/history.json"

if not os.path.exists(file_path):
    st.warning("Belum ada data riwayat pemindaian.")
else:
    with open(file_path, "r") as f:
        lines = f.readlines()

    if not lines:
        st.info("Riwayat kosong.")
    else:
        history_data = [json.loads(line) for line in reversed(lines)]
        
        # Menampilkan 2 kolom per baris
        for i in range(0, len(history_data), 2):
            cols = st.columns(2)
            
            # Helper untuk merender kartu agar kode rapi
            def render_card(data):
                weather = data.get('weather', 'N/A').lower()
                icon = "☀️" if "cerah" in weather else "☁️"
                return f"""
                <div class='metric-card'>
                    <div style='display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 15px;'>
                        <span style='font-size: 2em;'>{icon}</span>
                        <span style='font-size: 1.4em; font-weight: 800; color: #9a3412;'>{data.get('weather', 'N/A').upper()}</span>
                    </div>
                    <div style='border-top: 1px solid #e5e7eb; padding-top: 10px;'>
                        <div style='display: flex; justify-content: space-between; margin: 5px 0;'>
                            <span style='color: #6b7280;'>🌡️ Suhu Udara</span>
                            <span style='font-weight: 700;'>{data.get('temperature', '0')} °C</span>
                        </div>
                        <div style='display: flex; justify-content: space-between; margin: 5px 0;'>
                            <span style='color: #6b7280;'>🎯 Tingkat Keyakinan</span>
                            <span style='font-weight: 700; color: #059669;'>{data.get('confidence', '0')}%</span>
                        </div>
                    </div>
                </div>
                """

            with cols[0]:
                st.markdown(render_card(history_data[i]), unsafe_allow_html=True)
                
            if i + 1 < len(history_data):
                with cols[1]:
                    st.markdown(render_card(history_data[i+1]), unsafe_allow_html=True)

# --- TOMBOL NAVIGASI ---
if st.button("⬅️ Kembali ke Home"):
    st.switch_page("app.py")