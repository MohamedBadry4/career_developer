# 🧑‍💻 PathCoder – Developer Career Path Recommender

A cross-platform AI-powered web app that helps developers explore career paths, predict suitable jobs, and discover skills they need to grow.

---

## 📘 About the Project

Developers often struggle to identify the right career track and the skills required to advance. **PathCoder** is a machine learning–powered application that predicts the most suitable career track for developers based on their current skills and recommends additional skills to master.

The system leverages:

* **Random Forest** for job prediction
* **Recommendation Engine** for skill suggestions
* **Flask API** for backend inference & integration
* **Streamlit** for an interactive frontend
* **MLflow** for experiment tracking and model management
* **Firebase** for user authentication
* **MySQL** for structured data storage

---

## 🚀 Features

* ✍️ Input your current technical skills
* 🎯 Predict the most suitable career track (e.g., Web Developer, Data Scientist, AI Engineer)
* 💡 Receive personalized skill recommendations
* 🤖 Chatbot assistance for developer career questions
* 📊 Explore explainable predictions (feature importance, SHAP)
* 💾 Track and version ML models with MLflow
* 🔐 User authentication with Firebase
* 🌐 Lightweight, interactive, and user-friendly UI with Streamlit

---

## 🧠 AI Models Used

| Task                              | Model                           | Framework        | Notes                                      |
| --------------------------------- | ------------------------------- | ---------------- | ------------------------------------------ |
| Career Prediction                 | Random Forest                   | Scikit-learn     | Balanced with class weights                |
| Skill Recommendation              | Rule-based + similarity metrics | Python           | Suggests skills based on chosen track      |
| Emotion Detection (extra feature) | TensorFlow CNN (SER)            | TensorFlow/Keras | Analyzes speech tone to enrich interaction |

---

## 🗂️ Dataset & Preprocessing

**Sources:** Stack Overflow Developer Survey + curated skill-job datasets
**Categories:** Developer roles (Web Developer, Data Scientist, ML Engineer, etc.)

**Steps:**

* Cleaned inconsistent responses
* Converted multi-label skills into binary encoding
* Removed non-technical roles and outliers
* Augmented dataset with domain knowledge
* Standardized formats for tools & languages

---

## 🧪 Testing Overview

| Layer         | Tools/Methods                         |
| ------------- | ------------------------------------- |
| Model Testing | Accuracy, Precision, Recall, F1-score |
| API Testing   | Postman + Flask error handling        |
| Load Testing  | Locust.io stress testing              |
| App Testing   | Unit testing + UAT with developers    |

---

## 🧱 System Architecture

**PathCoder Workflow:**

1. **Streamlit Frontend** → Developer inputs skills
2. **Flask API** → Predicts job + recommends skills
3. **MLflow** → Tracks experiments & stores models
4. **MySQL Database** → Stores user data and history
5. **Firebase Auth** → Manages secure login
6. **Chatbot (NLP model)** → Assists users with questions

---

## 🧑‍💻 Technologies Used

| Layer       | Stack                             |
| ----------- | --------------------------------- |
| Frontend    | Streamlit (Python)                |
| Backend     | Flask (Python)                    |
| Auth        | Firebase Authentication           |
| Database    | MySQL                             |
| ML Training | Jupyter, Scikit-learn, TensorFlow |
| Tools       | MLflow, OpenCV, PyCharm           |

---
