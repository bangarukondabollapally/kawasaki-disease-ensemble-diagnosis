from flask import Flask, render_template, request
import numpy as np
import pickle

# 1️⃣ Create Flask app FIRST
app = Flask(__name__)

# 2️⃣ Load model
with open("weighted_ensemble_model.pkl", "rb") as f:
    model_data = pickle.load(f)

# 3️⃣ Home route
@app.route('/')
def home():
    return render_template("index.html")

# 4️⃣ Predict route
@app.route('/predict', methods=['POST'])
def predict():

    features = []
    for i in range(12):
        value = float(request.form[f"f{i}"])
        features.append(value)

    features = np.array(features).reshape(1, -1)

    gb_pred = model_data["gb_model"].predict_proba(features)
    ada_pred = model_data["ada_model"].predict_proba(features)

    final_prob = (
        model_data["weight_gb"] * gb_pred +
        model_data["weight_ada"] * ada_pred
    )

    prediction = np.argmax(final_prob)

    return render_template("result.html", prediction=prediction)

# 5️⃣ Run app
if __name__ == "__main__":
    app.run(debug=True)
