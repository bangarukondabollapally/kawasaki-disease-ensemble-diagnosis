🩺 Kawasaki Disease Diagnosis Using Feature-Optimized Weighted Ensemble Model

A machine learning-based medical diagnosis system that predicts the risk of Kawasaki Disease using Modified Grey Wolf Optimization (MGWO) for feature selection and a weighted ensemble of Gradient Boosting and AdaBoost classifiers. The trained model is deployed using a Flask web application for real-time prediction.

📌 Table of Contents

Project Overview

Features Used

Model Workflow

Project Structure

Installation & Setup

Running the Application

Evaluation Metrics

Future Improvements

Disclaimer

📖 Project Overview

This project focuses on building an intelligent disease prediction system by:

Performing data preprocessing and encoding

Selecting optimal features using MGWO

Training individual machine learning models

Combining models using a weighted ensemble strategy

Deploying the trained model using Flask

The goal is to improve diagnostic accuracy while maintaining model stability and interpretability.

🧠 Selected Features (12)

The final optimized features used for prediction are:

Age at Diagnosis

Gender

Ethnicity

Location

Fever Duration

Symptoms

Laboratory Tests

Echocardiography

Treatment Approach

Clinical Outcomes

Complications

Long-Term Effects

⚙️ Model Workflow
1️⃣ Data Preprocessing

Handling missing values

Encoding categorical variables

Feature preparation

2️⃣ Feature Optimization

Modified Grey Wolf Optimization (MGWO)

Selection of most relevant predictive attributes

3️⃣ Individual Model Training

Gradient Boosting Classifier

AdaBoost Classifier

4️⃣ Weighted Ensemble Strategy

Final prediction probability is calculated as:

Final_Probability =
(weight_gb × GB_Probability) + (weight_ada × ADA_Probability)

This improves performance by combining strengths of both models.

5️⃣ Model Serialization

Final ensemble model saved using pickle

Used for deployment in Flask application

🏗️ Project Structure
kawasaki-disease-ensemble-diagnosis/
│
├── app.py                         # Flask application
├── weighted_ensemble_model.pkl    # Serialized trained ensemble model
├── README.md                      # Project documentation
├── requirements.txt               # Required dependencies
│
└── templates/
    ├── index.html                 # User input form
    └── result.html                # Prediction output page

🚀 Installation & Setup
Step 1: Clone the Repository
git clone https://github.com/yourusername/kawasaki-disease-ensemble-diagnosis.git

Step 2: Navigate to Project Directory
cd kawasaki-disease-ensemble-diagnosis

Step 3: Install Required Libraries
pip install -r requirements.txt


If requirements file is unavailable:

pip install flask numpy pandas scikit-learn matplotlib

▶️ Running the Application

Run the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Enter patient details and generate prediction results.

📊 Evaluation Metrics

The model performance was evaluated using:

Accuracy

Precision

Recall

F1 Score

ROC Curve

Confusion Matrix

🔮 Future Improvements

Integrate SHAP for model interpretability

Improve ensemble with stacking techniques

Deploy on cloud platforms (Render / AWS)

Validate using real-world clinical datasets

Add database integration

⚠ Disclaimer

This project is developed for academic and research purposes only.
It is not intended for real-world medical diagnosis without professional validation.

👨‍💻 Author

Developed as part of an academic project on AI-based healthcare prediction systems.
