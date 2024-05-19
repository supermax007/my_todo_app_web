import streamlit as st
from PIL import Image


uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_uploaded_img = img.convert('L')
    st.image(gray_uploaded_img)

with st.expander('Start Camera'):
    camera_image = st.camera_input("Camera")

#Start the Camera
    if camera_image:
# Create a pillow image instance
        img = Image.open(camera_image)

#Conver pillow image to grayscale
        gray_img = img.convert("L")
#Render grayscale image
        st.image(gray_img)
        st.header("BAWWWWWS")


