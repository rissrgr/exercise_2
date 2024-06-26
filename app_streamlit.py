import streamlit as st
import requests

st.title("Permainan Tebak Angka Ganjil atau Genap")

angka_pertama = st.number_input('Masukkan angka pertama:', min_value=0, value=0)
angka_kedua = st.number_input('Masukkan angka kedua:', min_value=0, value=0)

if st.button("convert"):
    try:

        response = requests.post(
            "https://ed0c-103-82-14-56.ngrok-free.app/convert",
            json={"angka_pertama": angka_pertama, "angka_kedua": angka_kedua}
        )
    except Exception as e :
        print("Exception", e)
        st.error("Error in conversion")
    
    if response.status_code == 200:
        result = response.json()
        st.write("Hasil:")
        for item in result['hasil']:
            st.write(item)
    else:
        st.error("Error in conversion")