import streamlit as st
import requests
import os
from dotenv import load_dotenv

if os.path.isfile('.env'):
    load_dotenv()

API_FLASK_CONVERT = "https://ed0c-103-82-14-56.ngrok-free.app/convert" if os.getenv("API_FLASK_CONVERT") is None else os.getenv("API_FLASK_CONVERT")

st.title("Permainan Tebak Angka Ganjil atau Genap")

angka_pertama = st.number_input('Masukkan angka pertama:', min_value=0, value=0)
angka_kedua = st.number_input('Masukkan angka kedua:', min_value=0, value=0)

if st.button("Tampilkan Hasil"):
    response = requests.post(
        API_FLASK_CONVERT,
        json={"angka_pertama": angka_pertama, "angka_kedua": angka_kedua}
    )
    
    if response.status_code == 200:
        result = response.json()
        st.write("Hasil:")
        for item in result['hasil']:
            st.write(item)
    else:
        st.error("Error in conversion")