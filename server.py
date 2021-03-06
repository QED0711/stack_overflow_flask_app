import flask
from flask import Flask, request
from flask_cors import CORS

import pickle
from construct_model import *
from text_pre_processor import *

with open('./lg_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

application = Flask(__name__)

CORS(application)

print(lr_model)

@application.route('/', methods=['POST'])
def predict():
    print(request.json)

    user_input = request.json["user_input"]
    prediction = lr_model.get_prediction(user_input)[0]
    
    proba = lr_model.get_prediction(user_input, "proba")

    print(prediction, proba)
    
    return flask.jsonify({"prediction": prediction, "proba": proba})


if __name__ == "__main__":
    application.run(host='0.0.0.0')