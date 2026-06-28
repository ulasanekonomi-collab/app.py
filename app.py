import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="Neuroeconomics Lab", page_icon="🧠", layout="wide")

# Header Aplikasi
st.title("🧠 Neuroeconomics Interactive Learning App")
st.caption("Memahami bagaimana otak Anda mengambil keputusan ekonomi | Oleh: Yuhka Sundaya")
st.markdown("---")

# Sidebar untuk Navigasi
menu = st.sidebar.radio("Pilih Modul Pembelajaran:", ["1. Live Experiment: Ultimatum Game", "2. Teori: Anatomi Keputusan"])

# ------------------------------------------------------------------
# MODUL 1: ULTIMATUM GAME
# ------------------------------------------------------------------
if menu == "1. Live Experiment: Ultimatum Game":
    st.header("🎮 Laboratorium Mini: The Ultimatum Game")
    st.write(
        """
        Bayangkan Anda dan sebuah Bot AI menerima dana hibah sebesar **Rp1.000.000**. 
        Aturannya sederhana:
        1. Bot akan menentukan bagaimana uang tersebut dibagi antara Anda berdua.
        2. Anda hanya punya dua pilihan: **MENERIMA** atau **MENOLAK** tawaran tersebut.
        3. Jika Anda **Menerima**, uang dibagi sesuai tawaran.
        4. Jika Anda **Menolak**, uang hangus dan kalian berdua mendapat **Rp0**.
        """
    )
    
    st.info("**Skenario:** Bot mengambil Rp800.000 untuk dirinya sendiri, dan menawarkan **Rp200.000** untuk Anda.")
    
    # Tombol Keputusan
    col1, col2 = st.columns(2)
    with col1:
        terima = st.button("✅ Terima (Dapat Rp200.000)", use_container_width=True)
    with col2:
        tolak = st.button("❌ Tolak (Kedua pihak dapat Rp0)", use_container_width=True)
        
    # Logika Hasil
    if terima:
        st.success("💰 Anda memutuskan untuk **MENERIMA**. Anda membawa pulang Rp200.000 dan Bot mendapat Rp800.000.")
        st.markdown("### 🧠 Apa yang Terjadi di Otak Anda?")
        st.write(
            """
            Secara ekonomi klasik (*Homo Economicus*), keputusan Anda 100% rasional. Lebih baik dapat Rp200.000 daripada tidak sama sekali. 
            Saat Anda memilih ini, **Dorsolateral Prefrontal Cortex (dlPFC)** Anda aktif untuk menekan emosi negatif dan mengedepankan logika kalkulasi keuntungan.
            """
        )
        
    if tolak:
        st.error("💥 Anda memutuskan untuk **MENOLAK**. Uang hangus! Anda mendapat Rp0 dan Bot mendapat Rp0.")
        st.markdown("### 🧠 Apa yang Terjadi di Otak Anda?")
        st.write(
            """
            Secara teori ekonomi murni, tindakan Anda ini 'tidak rasional' karena Anda membuang uang gratis. Namun, secara psikologi dan neurosains, ini adalah respons manusiawi yang normal!
            
            Saat Anda melihat tawaran tidak adil (Rp800k vs Rp200k), bagian otak bernama **Anterior Insula** aktif secara agresif. Bagian ini mendeteksi rasa muak (sama seperti saat Anda mencium bau busuk) dan ketidakadilan. Rasa muak ini mengalahkan logika Anda, membuat Anda rela rugi demi menghukum Bot yang serakah.
            """
        )

# ------------------------------------------------------------------
# MODUL 2: ANATOMI KEPUTUSAN
# ------------------------------------------------------------------
elif menu == "2. Teori: Anatomi Keputusan":
    st.header("🧠 Anatomi Otak dalam Pengambilan Keputusan")
    st.write("Geser slider di bawah ini untuk melihat area otak mana yang mendominasi keputusan finansial Anda.")
    
    # Slider Emosi vs Logika
    kondisi = st.slider("Kondisi Penawaran Finansial:", min_value=1, max_value=3, value=2, 
                        format="")
    st.labels = {1: "Sangat Merugikan/Diskon Palsu", 2: "Netral", 3: "Dapat Jackpot/Diskon Besar"}
    
    if kondisi == 1:
        st.subheader("🔴 Sistem Risiko & Rasa Sakit Aktif")
        st.warning("**Area Otak: Insula Cortex**")
        st.write("Ketika Anda melihat harga produk yang kemahalan atau merasa ditipu, Insula akan aktif. Otak merespons kehilangan uang dengan pola yang mirip dengan rasa sakit fisik.")
        
    elif kondisi == 2:
        st.subheader("🟡 Kondisi Seimbang (Homeostasis)")
        st.info("**Area Otak: Prefrontal Cortex (PFC)**")
        st.write("Otak melakukan komparasi fungsional biasa antara harga barang dan nilai manfaatnya. Logika berjalan normal.")
        
    elif kondisi == 3:
        st.subheader("🟢 Sistem Imbalan (Reward System) Meledak")
        st.success("**Area Otak: Nucleus Accumbens / Ventral Striatum**")
        st.write("Melihat diskon besar atau keuntungan instan memicu pelepasan dopamin di Ventral Striatum. Ini menciptakan dorongan impulsif untuk membeli atau mengeksekusi investasi saat itu juga.")
