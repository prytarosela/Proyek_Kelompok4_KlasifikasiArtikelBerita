import streamlit as st
from joblib import load

# Memuat model dan vectorizer
model = load("model/naive_bayes_model.joblib")
vectorizer = load("model/tfidf_vectorizer.joblib")

# Antarmuka Streamlit
st.title("Klasifikasi Artikel Berita")
input_text = st.text_area("Masukkan teks berita di sini:")

if st.button("Klasifikasikan"):
    if input_text:
        input_vector = vectorizer.transform([input_text])
        prediction = model.predict(input_vector)[0]
        label_map = {0: "World", 1: "Sports", 2: "Business", 3: "Sci/Tech"}
        st.write(f"Kategori Prediksi: **{label_map[prediction]}**")
    else:
        st.write("Harap masukkan teks berita.")