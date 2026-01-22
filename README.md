Fashion MNIST Classification — ANN
📌 Overview

This project implements an Artificial Neural Network (ANN) to classify clothing images from the Fashion-MNIST dataset — a benchmark dataset of 28×28 grayscale fashion item images from 10 categories.

The purpose is to demonstrate data preprocessing, model building, training, evaluation, and visualization using deep learning fundamentals.

📦 Dataset

Fashion-MNIST is a drop-in replacement for the classic MNIST dataset with more challenging fashion images, consisting of:

70,000 total images (60,000 train + 10,000 test)

10 classes of clothing items

Each image is 28×28 pixels, grayscale

Label	Description
0	T-shirt/top
1	Trouser
2	Pullover
3	Dress
4	Coat
5	Sandal
6	Shirt
7	Sneaker
8	Bag
9	Ankle boot
🧠 Model

This repository uses a Feedforward Neural Network (ANN) with:

Input layer — flattened vector of image pixels

One or more hidden dense layers with ReLU activation

Softmax output layer for 10-class classification

🛠️ Tech Stack

Python

NumPy

TensorFlow / Keras

Matplotlib

Scikit-learn

Jupyter Notebook

📋 Getting Started
📥 Clone Repository
git clone https://github.com/lequangduyet03/fashion-mnist-ann.git
cd fashion-mnist-ann

📖 Open Notebook

Use Jupyter Notebook or JupyterLab:

jupyter notebook fashion_mnist_ann.ipynb

🧪 Workflow Steps

Import and analyze Fashion MNIST dataset
Using Keras or TensorFlow utilities to load images & labels.

Data preprocessing

Normalize pixel intensities

Flatten images for ANN input

Build ANN model

Dense layers

ReLU activations

Softmax on output

Train & Evaluate

Train on train dataset

Evaluate accuracy and loss on test dataset

Visualize results

Plot accuracy/loss curves

Display sample predictions

📊 Results & Metrics

Describe here your final training and test accuracy, loss curves, confusion matrix or other metrics.

(e.g., “Test accuracy: ~92%” or “Loss stabilized after 20 epochs”)

🧠 Learnings

Preprocessing images for ML models

Building ANN with Keras

Visualization of training dynamics

Limitations of ANN on image data

🚀 Future Improvements

Use Convolutional Neural Network (CNN) for better accuracy

Hyperparameter tuning

Save model weights + inference script

Add interactive demo or deployment

👤 Author

lequangduyet03 - [GitHub](https://github.com/lequangduyet03)
