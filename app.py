from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def home():
    return "API Prediksi Kelulusan Mahasiswa"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    return jsonify({"prediksi_lulus": int(pred)})

if __name__ == '__main__':
    app.run(debug=True)
