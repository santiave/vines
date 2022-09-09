import streamlit as st
from paddleocr import PaddleOCR, draw_ocr
from matplotlib import pyplot as plt
import cv2
import os
import numpy as np



ocr = PaddleOCR()
img=None
img=st.camera_input('vin')
if img == None:
    img=st.file_uploader('vin')
if img is not None:
    bytes_data = img.getvalue()
    img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    result=ocr.ocr(img)
    st.write(f'VIN: {"".join(i for i in result[0][1][0] if (i.isascii() and i.isalnum())) }')
    st.write(f'ACCURACY: {result[0][1][1]:.1%}')
    
  
