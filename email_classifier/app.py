
from flask import Flask, render_template, request
import joblib
import os
import pandas as pd

from preprocessing import (
    text_preprocessing,
    special_char,
    digit,
    capital
)


app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

models = {
    "naive_bayes_bow": joblib.load(
        os.path.join(MODEL_DIR, "naive_bayes.pkl")
    ),

    "random_forest_bow": joblib.load(
        os.path.join(MODEL_DIR, "random_forest.pkl")
    ),

    "logistic_regression_bow": joblib.load(
        os.path.join(MODEL_DIR, "logestic.pkl")
    ),

    "naive_bayes_tfidf": joblib.load(
        os.path.join(MODEL_DIR, "naive_bayes2.pkl")
    ),

    "random_forest_tfidf": joblib.load(
        os.path.join(MODEL_DIR, "random_forest2.pkl")
    ),

    "logistic_regression_tfidf": joblib.load(
        os.path.join(MODEL_DIR, "logistic2.pkl")
    )
}

print("All ML models loaded successfully!")



def select_model(model_name, vectorizer_name):

    model_key = f"{model_name}_{vectorizer_name}"

    return models.get(model_key)


def extract_features(message):

    clean_message = text_preprocessing(message)

    features = {
        "clean_message": clean_message,
        "total_words": len(clean_message.split()),
        "char_count": len(message),
        "special_char": special_char(message),
        "digit_count": digit(message),
        "capital_letters": capital(message)
    }

    return pd.DataFrame([features])


def make_prediction(message, selected_model, selected_vectorizer):

    selected_pipeline = select_model(
        selected_model,
        selected_vectorizer
    )

    if selected_pipeline is None:
        raise ValueError("Invalid model or vectorizer selection")

    input_data = extract_features(message)

    prediction = selected_pipeline.predict(input_data)

    return prediction[0]


@app.route("/")
def home():

    return render_template("index.html")




@app.route("/predict", methods=["POST"])
def predict():

    message = request.form.get("message", "").strip()
    model = request.form.get("model", "")
    vectorizer = request.form.get("vectorizer", "")

    if not message:
        return {"error": "Please enter a message"}, 400

    try:
        prediction = make_prediction(message, model, vectorizer)

        if prediction == 0:
            result = "Spam"
        elif prediction == 1:
            result = "Ham"
        else:
            result = str(prediction)

        return {
            "prediction": result,
            "model": model,
            "vectorizer": vectorizer,
            "message": message
        }

    except Exception as error:
        print("Prediction Error:", error)
        return {"error": "Prediction failed"}, 500


if __name__ == "__main__":

    app.run(debug=True)
