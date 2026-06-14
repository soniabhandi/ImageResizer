import streamlit as st
import cv2
import numpy as np

st.title("Image Resizer")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

scale_percent = st.slider(
    "Resize Percentage",
    10,
    100,
    50
)

if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    new_width = int(
        image.shape[1] * scale_percent / 100
    )

    new_height = int(
        image.shape[0] * scale_percent / 100
    )

    new_size = (
        new_width,
        new_height
    )

    output = cv2.resize(
        image,
        new_size
    )

    st.subheader("Original Image")
    st.image(
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    )

    st.subheader("Resized Image")
    st.image(
        cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    )

    _, buffer = cv2.imencode(
        ".png",
        output
    )

    st.download_button(
        label="Download Resized Image",
        data=buffer.tobytes(),
        file_name="resized_image.png",
        mime="image/png"
    )