
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

st.title("Image Classification App")

uploaded_file = st.file_uploader("Upload Image", type=['jpg','png'])
if uploaded_file:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    if st.button("Classify"):
        model = load_model('cat_dog_model.h5')  # Pretrained model
        img = image.load_img(uploaded_file, target_size=(64,64))
        x = image.img_to_array(img)/255.0
        x = np.expand_dims(x, axis=0)
        pred = model.predict(x)
        st.success(f"Prediction: {'Dog' if pred[0][0]>0.5 else 'Cat'}")