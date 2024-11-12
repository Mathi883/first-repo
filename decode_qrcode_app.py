import streamlit as st
import numpy as np
import cv2

def decode_qrcode():

    #add a headerç
    st.header("Test")

    #add a file uploader widget
    qrcode = st.file_uploader("Upload your QR Code",
                     type=['jpg','png','jpeg'])

    if qrcode:

        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        #place the qr code
        st.image(opencv_image)

        #decode the qr code
        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your QRCode contained {decoded_info}")
        st.write(straight_qr)