import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open("templates/model.pkl", "rb"))


@app.route("/predict", methods = ["post"])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    prediction = model.predict(query_df)
    return jsonify({"Prediction": list(prediction)})

if __name__=="__main__":
    app.run(debug=True)
 