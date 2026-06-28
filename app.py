import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Aplikasi Pembelajaran Neuroeconomics", page_icon="🧠", layout="wide")

# Gaya CSS Khusus
st.markdown("""
    <style>
    .main-title { font-size:32px; font-weight:bold; color:#2E4053; margin-bottom:5px; }
    .subtitle { font-size:18px; color:#5D6D7E; margin-bottom:20px; }
    .brain-box { padding:15px; background-color:#FBEEE6; border-left:6px solid #E67E22; border-radius:4px; margin-bottom:15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🧠 Neuroeconomics Interactive Learning Laboratory</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Mengintegrasikan Model Formal Ekonomi dengan Sistem Kognitif Otak (Referensi: Glimcher et al., 2009)</p>', unsafe_allow_html=True)
st.markdown("---")

# 2. NAVIGASI UTAMA (BERDASARKAN STRUKTUR BAB BUKU)
menu = st.sidebar.selectbox(
    "Pilih Modul Pembelajaran:",
    [
        "Pengantar & Sejarah",
        "Modul 1: Teori Keputusan Aksiomatik (Bab 3 & 4)",
        "Modul 2: Teori Permainan Non-Kooperatif (Bab 5 & 6)",
        "Modul 3: Reward Prediction Error / RPE (Bab 3)"
    ]
)

# ==================================================================
# MODUL PENGANTAR
# ==================================================================
if menu == "Pengantar & Sejarah":
    st.subheader("📚 Jembatan Dua Disiplin Ilmu")
    st.write("""
    Aplikasi ini dirancang sebagai alat bantu ajar interaktif untuk menjembatani **Ekonomi Neoklasikal** (yang berfokus pada hasil akhir pilihan/*Revealed Preference*) dan **Cognitive Neuroscience** (yang berfokus pada proses algoritma biologis di dalam otak).
    """)

# ==================================================================
# MODUL 1: TEORI KEPUTUSAN AKSIOMATIK (BAB 3 & 4)
# ==================================================================
elif menu == "Modul 1: Teori Keputusan Aksiomatik (Bab 3 & 4)":
    st.header("⚖️ Eksperimen Maksimisasi Utilitas & Risiko Dinamis")
    st.write("""
    Berdasarkan Bab 4 (Aldo Rustichini), otak kita memproses keputusan ekonomi melalui dua tahap: 
    **Evaluasi Nilai (Utilitas)** dan **Komparasi Kuantitas** melalui model *Random Walk* dengan hambatan endogen.
    """)
    
    st.subheader("Simulasi Lotere Von Neumann-Morgenstern")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("**Atur Parameter Lotere Anda:**")
        p_jackpot = st.slider("Probabilitas Mendapat Jackpot (p)", 0.0, 1.0, 0.5, 0.05)
        val_jackpot = st.number_input("Nilai Uang Jackpot (Rp)", value=500000, step=50000)
        alpha = st.slider("Tingkat Risk Aversion (α) | 1=Rasional murni, <1=Takut Risiko", 0.1, 1.0, 0.7, 0.05)
        
        # Perhitungan Nilai Utilitas Berdasarkan Fungsi Kekayaan Khas Ekonomi Perilaku
        expected_value = p_jackpot * val_jackpot
        utility = p_jackpot * (val_jackpot ** alpha)
        
    with col2:
        st.metric(label="Nilai Harapan Objektif (Expected Value)", value=f"Rp {expected_value:,.0f}")
        st.metric(label="Utilitas Subjektif di Otak (U)", value=f"{utility:,.2f} unit")
        
        # Plotting Kurva Utilitas Noisy perception
        x_vals = np.linspace(0, 1000000, 100)
        y_vals = x_vals ** alpha
        df_curve = pd.DataFrame({'Nilai Uang': x_vals, 'Utilitas': y_vals})
        fig = px.line(df_curve, x='Nilai Uang', y='Utilitas', title="Fungsi Utilitas Subjektif Otak")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div class="brain-box">
        <strong>🧠 Catatan Neurosains (Bab 4):</strong><br>
        Ketika Anda mengubah parameter risiko di atas, rekaman unit tunggal pada primata menunjukkan 
        bahwa <strong>Lateral Intraparietal Area (Area LIP)</strong> bertugas memetakan peta utilitas 
        terhadap ruang visual target pilihan tersebut.
    </div>
    """, unsafe_allow_html=True)

# ==================================================================
# MODUL 2: TEORI PERMAINAN NON-KOOPERATIF (BAB 5 & 6)
# ==================================================================
elif menu == "Modul 2: Teori Permainan Non-Kooperatif (Bab 5 & 6)":
    st.header("🎮 Laboratorium Game Theory Eksperimental")
    st.write("Eksperimen interaktif interaksi sosial menggunakan basis data empiris Bab 5 & 6.")
    
    game_choice = st.selectbox("Pilih Jenis Permainan:", ["The Ultimatum Game (Bargaining)", "The Trust Game (Reciprocity)"])
    
    if game_choice == "The Ultimatum Game (Bargaining)":
        st.subheader("Skenario: Pembagian Uang Rp 1.000.000")
        st.warning("Bot menawarkan pembagian tidak adil: **Bot ambil Rp 800.000, Anda diberi Rp 200.000**.")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Terima Saja"):
                st.success("Anda memilih rasional secara ekonomi klasik. Logika mengalahkan emosi.")
                st.markdown("""
                <div class="brain-box">
                    <strong>🧠 Analisis Pemindaian fMRI (Sanfey et al., 2003):</strong><br>
                    Saat menerima tawaran ini, terjadi aktivitas kuat di <strong>Dorsolateral Prefrontal Cortex (dlPFC)</strong> 
                    yang berfungsi melakukan kendali kognitif untuk menekan emosi negatif demi mendapatkan keuntungan materi.
                </div>
                """, unsafe_allow_html=True)
        with c2:
            if st.button("❌ Tolak (Kedua Pihak Dapat Rp 0)"):
                st.error("Anda menghukum Bot yang serakah meskipun Anda harus rugi uang.")
                st.markdown("""
                <div class="brain-box">
                    <strong>🧠 Analisis Pemindaian fMRI (Sanfey et al., 2003):</strong><br>
                    Penolakan ini didorong oleh letupan aktivitas agresif di <strong>Anterior Insula</strong>. 
                    Area ini memproses rasa muak secara fisik (seperti mencium bau busuk) dan ketidakadilan sosial. 
                    Jika aktivitas Insula lebih tinggi daripada dlPFC, Anda pasti menolak!
                </div>
                """, unsafe_allow_html=True)

    elif game_choice == "The Trust Game (Reciprocity)":
        st.subheader("Simulasi Investasi Sosial")
        dana_kirim = st.slider("Berapa banyak uang yang ingin Anda percayakan/investasikan ke Trustee? (Uang akan dikali 3)", 0, 100000, 50000, 10000)
        
        if st.button("Kirim Dana"):
            dana_termultiplikasi = dana_kirim * 3
            st.info(f"Uang yang diterima Trustee bermutasi menjadi **Rp {dana_termultiplikasi:,.0f}**")
            
            # Simulasi respons Bot berbasis probabilitas empiris buku
            st.success(f"Trustee mengembalikan **Rp {dana_kirim * 1.2:,.0f}** kepada Anda. Investasi sosial Anda berhasil!")
            st.markdown("""
            <div class="brain-box">
                <strong>🧠 Mekanisme Hormonal & Neurobiologis (Bab 5):</strong><br>
                Keputusan untuk mempercayai orang asing diatur oleh neuropeptida <strong>Oxytocin</strong> di dalam otak. 
                Pemberian oksitosin secara klinis terbukti meningkatkan volume dana investasi tanpa mengubah persepsi risiko subjek.
            </div>
            """, unsafe_allow_html=True)

# ==================================================================
# MODUL 3: REWARD PREDICTION ERROR / RPE (BAB 3)
# ==================================================================
elif menu == "Modul 3: Reward Prediction Error / RPE (Bab 3)":
    st.header("⚡ Sirkuit Dopaminergik & Algoritma Pembelajaran Otak")
    st.write("""
    Berdasarkan Bab 3 (Andrew Caplin & Mark Dean), salah satu penemuan terbesar neuroeconomics adalah pembuktian bahwa 
    sistem dopamin otak tidak mengodekan 'hadiah statis', melainkan **Reward Prediction Error (RPE)**.
    """)
    
    st.latex(r"RPE = \text{Reward Aktual} - \text{Reward Ekspektasi}")
    
    # Kalkulator Letupan Dopamin
    st.subheader("Kalkulator Letupan Sirkuit Dopamin")
    col_a, col_b = st.columns(2)
    with col_a:
        ekspektasi = st.slider("Ekspektasi Anda Terhadap Suatu Hasil", 0, 100, 50)
        aktual = st.slider("Hasil Aktual yang Anda Terima", 0, 100, 80)
        rpe = aktual - ekspektasi
    
    with col_b:
        if rpe > 0:
            st.success(f"📈 RPE Positif: +{rpe} | Dopamin meletup di atas *baseline* (Phasic Burst)!")
            st.write("Otak mendeteksi hasil yang lebih baik dari dugaan. Anda merasa sangat senang/jackpot.")
        elif rpe == 0:
            st.info(f"↕️ RPE Nol: {rpe} | Dopamin berjalan di tingkat *baseline* yang stabil.")
            st.write("Hasil sesuai ekspektasi. Tidak ada kejutan biologis.")
        else:
            st.error(f"📉 RPE Negatif: {rpe} | Sel dopamin mengalami pembekuan/jeda (*Dopamine Pause*).")
            st.write("Hasil di bawah ekspektasi. Muncul sinyal kekecewaan di area *Nucleus Accumbens*.")
# ==================================================================
# FOOTER (BAGIAN PALING BAWAH APLIKASI)
# ==================================================================
st.markdown("---")  # Membuat garis pemisah tipis
st.markdown(
    '<p style="text-align: center; color: #888888; font-size: 13px;">'
    'Dikembangkan oleh Yuhka Sundaya & Dewi Rosiana'
    '</p>', 
    unsafe_allow_html=True
)
