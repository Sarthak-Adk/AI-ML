from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and encoder
model = joblib.load("book_rating_model.pkl")
encoder = joblib.load("category_encoder.pkl")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    price = float(request.form['price'])
    stock = int(request.form['stock'])
    category = request.form['category']

    # encode category
    category_encoded = encoder.transform([category])[0]

    # create input dataframe
    input_data = pd.DataFrame({
        'price': [price],
        'stock': [stock],
        'category': [category_encoded]
    })

    prediction = model.predict(input_data)[0]

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)