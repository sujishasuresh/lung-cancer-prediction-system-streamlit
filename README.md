# 🫁 Lung Cancer Prediction System

A machine learning KNN-based lung cancer prediction system built with **Python and Streamlit**.

The trained K-Nearest Neighbors (KNN) model and StandardScaler are integrated into a Streamlit web application that allows users to enter patient-related information and receive a model-based prediction.

> ⚠️ **Disclaimer:** This application is developed for study and educational purposes only. The predictions may not be accurate and should not be considered a medical diagnosis.

---

## 📌 Project Overview

This project demonstrates the deployment of a trained machine learning classification model using Streamlit.

The application accepts the following inputs:

- Age
- Smoking
- Area Quality
- Alcohol Consumption

These values are processed using the saved **StandardScaler** and passed to the trained **KNN model** to generate a prediction.

---

## 🤖 Machine Learning Model

The prediction system uses:

**K-Nearest Neighbors (KNN)**

The model was trained and evaluated separately using the same dataset. KNN was selected for this Streamlit application after comparing it with a Naive Bayes model.

## 🛠️ Technologies Used

- Python
- Scikit-learn
- K-Nearest Neighbors (KNN)
- Streamlit
- Pickle
