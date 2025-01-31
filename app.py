from flask import Flask, request, jsonify
from flask_httpauth import HTTPTokenAuth
import numpy as np
import pandas as pd
import joblib
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    os.getenv("BEARER_TOKEN"): "user"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

combined_model = joblib.load("/app/models/chipmunk_dataset.joblib")

model_homerun = combined_model["homerun"]
model_strike = combined_model["strike"]

features_homerun = ['ExitVelocity', 'HitDistance', 'LaunchAngle']
features_strike = ['release_speed', 'release_spin_rate', 'pfx_x', 'pfx_z', 'plate_x', 'plate_z', 'zone']

@app.route('/', methods=['GET'])
def index():
    return 'her şeye seni yazdım, her şeyi sana yazdım :)'

@app.route('/predict', methods=['POST'])
@auth.login_required
def predict():
    data = request.json

    expected_features = 10

    if 'request_homerun' in data:
        request_homerun = data['request_homerun']
        homerun_new_data = pd.DataFrame([request_homerun], columns=features_homerun)
        homerun_expanded = pd.DataFrame(np.zeros((homerun_new_data.shape[0], expected_features)), columns=model_homerun.feature_names_in_)
        homerun_expanded[features_homerun] = homerun_new_data
        predictions_homerun = model_homerun.predict(homerun_expanded)
        return jsonify({"homerun_predictions": predictions_homerun.tolist()})

    # elif :)
    elif 'request_strike' in data:
        request_strike = data['request_strike']
        strike_new_data = pd.DataFrame([request_strike], columns=features_strike)
        strike_expanded = pd.DataFrame(np.zeros((strike_new_data.shape[0], expected_features)), columns=model_strike.feature_names_in_)
        strike_expanded[features_strike] = strike_new_data
        predictions_strike = model_strike.predict(strike_expanded)
        return jsonify({"strike_predictions": predictions_strike.tolist()})

    else:
        return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1881)