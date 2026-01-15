import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import warnings
warnings.filterwarnings('ignore')


MODEL_PATH = "model.h5"
model = load_model(MODEL_PATH)

# Class labels
class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']



def detect_and_display(img, model, image_size=128):
    
    img = img.resize((image_size, image_size))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence_score = np.max(predictions, axis=1)[0]

    
    if class_labels[predicted_class_index] == 'notumor':
        result = " No Tumor Detected"
    else:
        result = f" !!!! Tumor Detected !!!! \n         ||         Type: {class_labels[predicted_class_index]}"

    return result, confidence_score, predictions


st.image("Brain_Tumor_Detector_Image.jpeg ", use_column_width=True)

st.title(" Brain Tumor Detection App")
st.write("Upload an MRI scan image and the model will detect the tumor type.")

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    
    img = load_img(uploaded_file)
    st.image(img, caption="Uploaded MRI", use_column_width=True)

    
    if st.button(" Detect Tumor"):
        result, confidence, preds = detect_and_display(img, model)

        st.subheader("Result:")
        st.success(result)
        st.write(f"**Confidence:** {confidence*100:.2f}%")

        
        st.subheader("Class Probabilities:")
        for i, prob in enumerate(preds[0]):
            st.write(f"{class_labels[i]}: {prob*100:.2f}%")
