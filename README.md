# Kawasaki Disease Diagnosis Using a Feature-Optimized Weighted Ensemble Model

## 📌 Overview

This project presents a machine learning-based diagnostic system for predicting Kawasaki Disease risk using a Feature-Optimized Weighted Ensemble Model.

The system integrates Modified Grey Wolf Optimization (MGWO) for feature selection and combines Gradient Boosting and AdaBoost classifiers using a weighted ensemble strategy to improve prediction accuracy and robustness.

A Flask-based web application is developed for real-time prediction.

---

## 🎯 Objectives

- Perform data preprocessing and feature engineering
- Apply Modified Grey Wolf Optimization (MGWO) for feature selection
- Train individual classifiers (Gradient Boosting & AdaBoost)
- Develop a Weighted Ensemble Model
- Evaluate model using ROC and Confusion Matrix
- Deploy model using Flask Web Application

---

## 🧠 Selected Features (12)

After dropping irrelevant columns, the following optimized features were selected:

1. Age at Diagnosis
2. Gender
3. Ethnicity
4. Location
5. Fever Duration
6. Symptoms
7. Laboratory Tests
8. Echocardiography
9. Treatment Approach
10. Clinical Outcomes
11. Complications
12. Long-Term Effects

---

## 🏗️ System Architecture

Data Preprocessing  
⬇  
Feature Optimization (MGWO)  
⬇  
Individual Classifier Training  
⬇  
Weighted Ensemble Model  
⬇  
Model Evaluation  
⬇  
Flask Deployment  

---

## ⚙️ Technologies Used

- Python
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- Flask
- Pickle (Model Serialization)

---

## 📊 Model Details

### Individual Models
- Gradient Boosting Classifier
- AdaBoost Classifier

### Ensemble Strategy
Final Prediction =  
(weight_gb × GB Probability) + (weight_ada × Ada Probability)

This approach improves prediction stability and reduces overfitting.

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC Curve
- Confusion Matrix

---

## 🌐 Web Application

The system includes a Flask-based web interface where users can:

- Enter patient details
- Select categorical medical attributes
- Predict Kawasaki Disease risk in real-time

---

## 📂 Project Structure

