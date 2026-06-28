import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# ==================================================================
# 1. KONFIGURASI HALAMAN & THEME ELEGAN
# ==================================================================
st.set_page_config(
    page_title="Neuroeconomics Lab", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk menyulap UI Streamlit menjadi tatap muka profesional
st.markdown("""
    <style>
    /* Mengubah font global ke inter/sans-serif */
    html, body, [data-testid="stSidebarView"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Desain Banner Atas */
    .hero-banner {
        background: linear-gradient(135deg, #1A252C 0%, #2C3E50 100%);
        padding: 30px;
        border-radius: 8px;
        color: #FFFFFF;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .hero-title { font-size: 30px; font-weight: 700; margin-bottom: 5px; letter-spacing: -0.5px; }
    .hero-subtitle { font-size: 15px; color: #BDC3C7; }
    
    /* Desain Kartu Teori (Academic Card) */
    .theory-card {
        background-color: #F8F9F9;
        border: 1px solid #E5E8E8;
        border-left: 4px solid #2980B9;
        padding: 20px;
        border-radius: 6px;
        margin-bottom: 20px;
    }
    
    /* Desain Insights Box */
    .insight-box {
        background-color: #EBF5FB;
        border: 1px solid #AED6F1;
        padding: 15px;
        border-radius: 6px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==================================================================
# 2. BANNER UTAMA
# ==================================================================
st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🧠 Neuroeconomics Interactive Lab</div>
        <div class="hero-subtitle">Platform Pembelajaran Proses Mekanisme Biologis dalam Pengambilan Keputusan Ekonomi</div>
    </div>
""", unsafe_allow_html=True)

# ==================================================================
# 3. SIDEBAR & NAVIGASI
# ==================================================================
st.sidebar.markdown("### 🗺️ Modul Akademik")
menu = st.sidebar.selectbox(
    "Pilih Topik Pembelajaran:",
    [
        "1. Pengantar & Model Paradigma",
        "2. Pilihan Aksiomatik & Risiko (Bab 3-4)",
        "3. Interaksi Sosial & Game Theory (Bab 5-6)",
        "4. Reward Prediction Error (Bab 3)"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.caption("Syllabus Reference:\n*Neuroeconomics: Decision Making and the Brain* (Glimcher et al.)")

# ==================================================================
# KONTEN MODUL 1: PENGANTAR
# ==================================================================
if menu == "1. Pengantar & Model Paradigma":
    st.markdown("### 📚 Menjembatani Utilitas Abstrak dengan Aktivitas Saraf")
    
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.write("""
        Selamat datang di Laboratorium Interaktif Neuroeconomics. Alat bantu ajar ini dirancang untuk membongkar kotak hitam (*black box*) pemikiran manusia saat berhadapan dengan insentif ekonomi. 
        
        Ekonomi neoklasik selama ini bertumpu pada asas *Revealed Preference*—menilai keputusan hanya dari apa yang dipilih. Sebaliknya, *Neuroeconomics* masuk lebih dalam untuk memetakan algoritma biologis yang terjadi di dalam sirkuit otak sebelum pilihan itu dieksekusi.
        """)
        
        st.markdown("""
        <div class="theory-card">
            <h4>Tiga Pilar Fondasi Pendekatan:</h4>
            <ol>
                <li><strong>Ekonomi:</strong> Menyediakan kerangka formal matematika dan konseptual (utilitas, maksimisasi, efisiensi).</li>
                <li><strong>Psikologi:</strong> Menyediakan pemahaman bias perilaku empiris, heuristik, dan keterbatasan kognitif.</li>
                <li><strong>Neurosains:</strong> Menyediakan alat ukur fisik sirkuit komputasi biologis (fMRI, single-unit recording, neurotransmiter).</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("### 🗺️ Arsitektur Sirkuit Pengambilan Keputusan")
        st.write("Secara mendasar, informasi dalam neuroekonomi mengalir melalui sirkuit berikut:")
        

# ==================================================================
# KONTEN MODUL 2: TEORI KEPUTUSAN AKSIOMATIK
# ==================================================================
elif menu == "2. Pilihan Aksiomatik & Risiko (Bab 3-4)":
    st.markdown("### ⚖️ Komputasi Risiko dan Kurva Utilitas Subjektif")
    
    st.markdown("""
    <div class="theory-card">
        Berdasarkan Bab 4 (Aldo Rustichini), otak tidak memproses angka kuantitatif mentah dari nilai uang, melainkan menerjemahkannya ke dalam skala representasi internal. Proses ini melibatkan pemetaan utilitas di area <strong>Lateral Intraparietal (LIP)</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown("##### ⚙️ Parameter Simulator")
        p_jackpot = st.slider("Probabilitas Hasil (p)", 0.0, 1.0, 0.5, 0.05)
        val_jackpot = st.number_input("Nilai Nominal Hadiah (Rp)", value=500000, step=50000)
        alpha = st.slider("Tingkat Risk Aversion (α)", 0.1, 1.0, 0.7, 0.05)
        
        expected_value = p_jackpot * val_jackpot
        utility = p_jackpot * (val_jackpot ** alpha)
        
        st.markdown("---")
        st.metric(label="Expected Value (Objektif)", value=f"Rp {expected_value:,.0f}")
        st.metric(label="Aktivitas Saraf / Utilitas Subjektif", value=f"{utility:,.2f} Unit")

    with col2:
        x_vals = np.linspace(0, 1000000, 100)
        y_vals = x_vals ** alpha
        df_curve = pd.DataFrame({'Nilai Uang': x_vals, 'Utilitas': y_vals})
        
        fig = px.line(df_curve, x='Nilai Uang', y='Utilitas', title="Kurva Utilitas Subjektif (Representasi di Otak)")
        fig.update_traces(line_color='#2980B9', line_width=3)
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=20, r=20, t=40, b=20),
            xaxis=dict(showgrid=True, gridcolor='#E5E8E8'),
            yaxis=dict(showgrid=True, gridcolor='#E5E8E8')
        )
        st.plotly_chart(fig, use_container_width=True)

# ==================================================================
# KONTEN MODUL 3: GAME THEORY
# ==================================================================
elif menu == "3. Interaksi Sosial & Game Theory (Bab 5-6)":
    st.markdown("### 🎮 Laboratorium Game Theory Eksperimental")
    
    game_choice = st.tabs(["The Ultimatum Game (Bargaining)", "The Trust Game (Reciprocity)"])
    
    with game_choice[0]:
        st.write("##### Skenario Pembagian Dana Hibah")
        st.write("Bot AI menawarkan proposal yang tidak adil: Dari total dana Rp 1.000.000, **Bot mengambil Rp 800.000 dan memberikan Anda Rp 200.000**.")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Terima Proposal", use_container_width=True):
                st.markdown("""
                <div class="insight-box">
                    <h5>🟢 Keputusan Diambil: Menerima</h5>
                    <p><strong>Analisis Neurokomputasi:</strong> Pilihan ini mencerminkan dominasi <strong>Dorsolateral Prefrontal Cortex (dlPFC)</strong>. Area ini melakukan kendali kognitif tingkat tinggi, menahan emosi negatif dari ketidakadilan demi memaksimalkan hasil ekonomi rasional.</p>
                </div>
                """, unsafe_allow_html=True)
        with c2:
            if st.button("❌ Tolak & Hanguskan", use_container_width=True):
                st.markdown("""
                <div class="insight-box" style="border-color:#F5B7B1; background-color:#FDF2F4;">
                    <h5>🔴 Keputusan Diambil: Menolak (Punishment)</h5>
                    <p><strong>Analisis Neurokomputasi:</strong> Mengapa manusia rela kehilangan uang gratis? Pemindaian fMRI menunjukkan letupan agresif di <strong>Anterior Insula</strong>. Area ini mendeteksi rasa muak (sama seperti mencium bau busuk fisik). Ketika sinyal Insula melampaui ambang batas dlPFC, manusia memilih menderita kerugian materi demi menghukum ketidakadilan (<i>nihil apresiasi</i> terhadap keseragaman sosial).</p>
                </div>
                """, unsafe_allow_html=True)
                
    with game_choice[1]:
        st.write("##### Simulasi Kepercayaan & Resiprositas")
        dana_kirim = st.slider("Dana yang Anda Percayakan ke Pihak Kedua (Uang otomatis berlipat 3x):", 0, 100000, 50000, 10000)
        
        if st.button("Kirim Investasi", use_container_width=True):
            st.info(f"Pihak kedua menerima dana yang termultiplikasi menjadi Rp {dana_kirim*3:,.0f}")
            st.success(f"Umpan balik: Pihak kedua mengembalikan Rp {dana_kirim*1.2:,.0f} kepada Anda.")
            st.markdown("""
            <div class="insight-box">
                <h5>🧬 Mekanisme Neuromodulator: Oxytocin</h5>
                <p>Keputusan untuk menaruh kepercayaan (*trust*) pada entitas asing sangat dimodulasi oleh hormon <strong>Oksitosin</strong>. Penelitian empiris menunjukkan peningkatan kadar oksitosin secara sengaja meningkatkan perilaku transfer dana sosial tanpa mengubah kalkulator penilaian risiko umum subjek.</p>
            </div>
            """, unsafe_allow_html=True)

# ==================================================================
# KONTEN MODUL 4: REWARD PREDICTION ERROR
# ==================================================================
elif menu == "4. Reward Prediction Error (Bab 3)":
    st.markdown("### ⚡ Sistem Dopaminergik & Algoritma Pembelajaran Otak")
    st.write("Salah satu pilar mekanistik terpenting dalam buku Paul Glimcher adalah pembuktian fungsi dopamin.")
    
    st.latex(r"\delta = R_{\text{actual}} - V_{\text{predicted}}")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("##### 🛠️ Kalkulator RPE")
        ekspektasi = st.slider("Ekspektasi/Prediksi Awal (V)", 0, 100, 50)
        aktual = st.slider("Hasil Nyata yang Diterima (R)", 0, 100, 80)
        rpe = aktual - ekspektasi
        
    with col_b:
        st.markdown("##### 🧬 Respons Sel Saraf")
        if rpe > 0:
            st.success(f"📈 RPE Positif: +{rpe}")
            st.write(" terjadi letupan frekuensi impuls (*Phasic Burst*) pada sel dopamin di area *Ventral Tegmental Area* (VTA). Ini adalah sinyal biologis untuk memperbarui memori: 'Tindakan ini menghasilkan sesuatu yang lebih baik dari dugaan!'")
        elif rpe == 0:
            st.info(f"↕️ RPE Nol: {rpe}")
            st.write("Sel dopamin tetap menembakkan impuls pada frekuensi dasar (*tonic baseline*). Tidak ada informasi baru yang perlu dipelajari oleh sirkuit kognitif.")
        else:
            st.error(f"📉 RPE Negatif: {rpe}")
            st.write("Terjadi penghentian sementara aktivitas sel (*Dopamine Pause*). Otak mendeteksi kekecewaan, mengirim isyarat sanksi internal agar sirkuit tidak mengulangi strategi pilihan tersebut di masa depan.")

# ==================================================================
# 4. FOOTER ELEGAN (CLARITY)
# ==================================================================
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #7F8C8D; font-size: 13px; letter-spacing: 0.5px;">'
    'Dikembangkan oleh Yuhka Sundaya & Dewi Rosiana'
    '</p>', 
    unsafe_allow_html=True
)
