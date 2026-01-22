Fashion MNIST Classification App (ANN + Streamlit)
📌 Project Overview

This project is a simple image classification web application built using an Artificial Neural Network (ANN) trained on the Fashion MNIST dataset.
The app allows users to select an image from the test set and view the predicted clothing category along with the model’s confidence score.

The application is deployed locally using Streamlit, providing an interactive interface for model inference.

🎯 Objectives

Train an ANN model to classify Fashion MNIST images

Build an end-to-end ML workflow:

Data loading & preprocessing

Model training & evaluation

Model deployment with Streamlit

Demonstrate practical ML deployment skills suitable for Data Intern / ML Intern roles

🗂️ Project Structure
├── app.py                     # Streamlit web application
├── fashion_mnist_ann.ipynb    # Model training & evaluation notebook
├── fashion_mnist_ann_model.h5 # Trained ANN model
├── README.md                  # Project documentation

📊 Dataset

Fashion MNIST

70,000 grayscale images (28x28)

10 clothing categories:

T-shirt/top

Trouser

Pullover

Dress

Coat

Sandal

Shirt

Sneaker

Bag

Ankle boot

🧠 Model

Type: Artificial Neural Network (ANN)

Framework: TensorFlow / Keras

Input: 28×28 grayscale images

Output: 10-class softmax probability distribution

🖥️ Web Application (Streamlit)
Features:

Select any test image using a slider

Visualize the selected image

Predict clothing category

Display prediction confidence

Technologies Used:

Streamlit

TensorFlow / Keras

NumPy

Matplotlib

🚀 How to Run the App
1️⃣ Install dependencies
pip install streamlit tensorflow numpy matplotlib

2️⃣ Run Streamlit app
streamlit run app.py

3️⃣ Open browser

Streamlit will automatically open at:

http://localhost:8501

📈 Example Output

Predicted Class: Sneaker

Confidence Score: 0.92

🛠️ Skills Demonstrated

Data preprocessing & normalization

Neural network modeling

Model inference

Interactive ML app deployment

Clean project structuring

ML-to-product thinking

👤 Author

lequangduyet03 - [GitHub](https://github.com/lequangduyet03)
