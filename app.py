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
    (tl, tr, br, bl) = result[0][0]
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))
    cv2.line(img, tl, tr, (0, 255, 0), 10)
    cv2.line(img, tr, br, (0, 255, 0), 10)
    cv2.line(img, br, bl, (0, 255, 0), 10)
    cv2.line(img, bl, tl, (0, 255, 0), 10)
    st.image(img)
    
  
