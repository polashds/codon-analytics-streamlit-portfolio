
import streamlit as st
import pandas as pd
from PIL import Image

st.title("Image Labeling App")

uploaded_files = st.file_uploader("Upload Images", type=['png','jpg'], accept_multiple_files=True)
labels = ['Cat','Dog','Other']
annotations = []

for img_file in uploaded_files:
    st.image(Image.open(img_file), caption=img_file.name)
    label = st.selectbox(f"Select label for {img_file.name}", labels, key=img_file.name)
    annotations.append({'image': img_file.name, 'label': label})

if st.button("Save Annotations"):
    df = pd.DataFrame(annotations)
    df.to_csv("image_labels.csv", index=False)
    st.success("Image annotations saved")