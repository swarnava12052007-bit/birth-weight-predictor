from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)

def clean_input_data(form_data):
    cleaned_data = {}
    for key, value in form_data.items():
        if isinstance(value, list):
            value = value[0]
        # Convert form strings to float or integer
        try:
            cleaned_data[key] = float(value)
        except ValueError:
            cleaned_data[key] = 0.0
    return cleaned_data

@app.route("/", methods=["GET"])
def home():
    return render_template("indexes.html")

@app.route("/predict", methods=["POST"])
def get_prediction():
    baby_data_form = request.form
    cleaned_data = clean_input_data(baby_data_form)
    
    baby_df = pd.DataFrame([cleaned_data])
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "model", "model.pkl")
    
    with open(model_path, "rb") as obj:
        model = pickle.load(obj)
        
    prediction = model.predict(baby_df)
    
    pred_val = prediction[0]
    if isinstance(pred_val, (list, np.ndarray)):
        pred_val = pred_val[0]
        
    prediction_rounded = round(float(pred_val), 2)
    
    # Send the result back to the HTML template
    return render_template("indexes.html", prediction=prediction_rounded)

if __name__ == "__main__":
    app.run(debug=True)
