import flask
from flask import Flask, request
from flask_cors import CORS

import pickle
from construct_model import *
from text_pre_processor import *

with open('./lg_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

app = Flask(__name__)

CORS(app)

print(lr_model)

@app.route('/', methods=['POST'])
def predict():
    print(request)

    user_input = request.json["user_input"]
    prediction = lr_model.get_prediction(user_input)[0]
    
    print(prediction)
    
    return flask.jsonify({"prediction": prediction})


