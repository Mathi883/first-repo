import streamlit as st
import segno as sg

st.title("Qr-Code Generator")


textinput = st.text_input("What text should be in the qr?")

if textinput:

    qrcode = sg.make_qr(textinput)
    qrcode.save("images/my_generated_qr_code.png")

