from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model + scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    # Get input
    cgpa = float(request.form['cgpa'])
    iq = float(request.form['iq'])

    # Convert to array
    input_data = np.array([[cgpa, iq]])

    # 🔥 SCALE INPUT (VERY IMPORTANT)
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Result
    result = "Placed 🎉" if prediction == 1 else "Not Placed ❌"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)