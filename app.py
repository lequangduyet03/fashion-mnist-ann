import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# Load streamlit run app.py

model = load_model("fashion_mnist_ann_model.h5")

# Class names
class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

st.title(" Fashion MNIST Classification App")
st.write("ANN-based image classification demo")

# Load dataset
(_, _), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# Select image
index = st.slider("Choose image index", 0, len(x_test) - 1, 0)

image = x_test[index]
label = y_test[index]

# Show image
st.subheader("Input Image")
fig, ax = plt.subplots()
ax.imshow(image, cmap="gray")
ax.axis("off")
st.pyplot(fig)

if st.button("Predict"):
    img = image / 255.0
    img = img.reshape(1, 28, 28, 1)

    prediction = model.predict(img)
    predicted_label = np.argmax(prediction)
    confidence = np.max(prediction)

    st.subheader("Prediction Result")
    st.success(f"Predicted: **{class_names[predicted_label]}**")
    st.write(f"Confidence: `{confidence:.2f}`")

