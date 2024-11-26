Proyek Akhir Klasifikasi Berita
Proyek ini adalah implementasi model pembelajaran mesin untuk mengklasifikasikan artikel berita ke dalam salah satu dari empat kategori: World, Sports, Business, dan Sci/Tech. Proyek ini menggunakan Naive Bayes untuk klasifikasi teks dan dilengkapi dengan antarmuka berbasis Streamlit.

Fitur Utama
Preprocessing Teks: Memproses data mentah menjadi bentuk yang siap digunakan untuk pelatihan model.
Klasifikasi Berita: Model Naive Bayes yang dilatih dengan dataset AG News untuk mengklasifikasikan teks berita.
Antarmuka Web: Aplikasi Streamlit untuk memudahkan pengguna melakukan klasifikasi berita berdasarkan input teks.

Kategori Berita
Dataset AG News terdiri dari empat kategori:
World: Berita internasional, diplomasi, dan konflik global.
Sports: Berita terkait pertandingan, atlet, dan perkembangan dunia olahraga.
Business: Berita keuangan, ekonomi, dan perusahaan.
Sci/Tech: Berita teknologi, inovasi, dan perkembangan ilmiah.

Persyaratan Sistem
Python: 3.8 atau lebih tinggi
Library Utama:
scikit-learn
pandas
datasets
streamlit

Instalasi
1. Clone Proyek
Clone repositori ke direktori lokal Anda:
git clone https://github.com/username/Proyek-Akhir-Klasifikasi-Berita.git
cd Proyek-Akhir-Klasifikasi-Berita
2. Buat Virtual Environment
Buat virtual environment dan aktifkan:
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate
3. Instal Dependensi
Instal semua library yang diperlukan:
pip install -r requirements.txt

Cara Menjalankan Proyek
1. Preprocessing dan Pelatihan Model
Untuk melakukan preprocessing dan melatih model:
python src/train.py
2. Evaluasi Model
Untuk mengevaluasi performa model:
python src/evaluate.py
3. Jalankan Aplikasi Streamlit
Untuk membuka antarmuka aplikasi:
streamlit run src/app.py

Buka browser Anda dan akses aplikasi di:
http://localhost:8501

Struktur Proyek
Proyek-Akhir-Klasifikasi-Berita/
├── data/                 # (Opsional) Folder untuk dataset (jika diunduh manual)
├── model/                # Folder untuk menyimpan model dan vectorizer
│   ├── naive_bayes_model.joblib
│   ├── tfidf_vectorizer.joblib
├── src/                  # Folder berisi kode utama
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   ├── app.py
├── requirements.txt      # Daftar dependensi
├── README.md             # Dokumentasi proyek

Panduan Penggunaan
Buka aplikasi Streamlit.
Masukkan teks berita di kolom input.
Klik Klasifikasikan untuk mendapatkan hasil prediksi kategori.

Referensi
Dataset: AG News Dataset (HuggingFace)
Library:
Scikit-learn Documentation
Streamlit Documentation
HuggingFace Datasets Documentation