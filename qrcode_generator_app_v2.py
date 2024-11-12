import streamlit as st
from decode_qrcode_app import decode_qrcode
from qrcodegenerator_page import qrcodegenerator

st.set_page_config(page_title="QR-Code Generator", page_icon="✨")

options = ['Generate QR Code', 'Decode QR Code', 'About me']
page_selection = st.sidebar.selectbox("Menu", options)

if page_selection == "Generate QR Code":
    qrcodegenerator()
elif page_selection == "Decode QR Code":
    decode_qrcode()
elif page_selection == "About me":
    st.title("About me")

