import flask
from flask import Flask, request
from flask_cors import CORS

import pickle
from construct_model import *
from text_pre_processor import *

with open('./lr_simple_model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST'])
def predict():
    print(request)
    user_input = request.json["user_input"]
    prediction = lr_model.get_prediction(user_input)[0]
    print(prediction)
    return flask.jsonify({"prediction": prediction})

###################
# JS AJAX REQUEST #
###################

# var settings = {
#   "async": true,
#   "crossDomain": true,
#   "url": "http://127.0.0.1:5000/",
#   "method": "POST",
#   "headers": {
#     "Content-Type": "application/json",
#     "cache-control": "no-cache",
#     "Postman-Token": "f426b0ab-9ae6-4897-823b-c59474ccefcd"
#   },
#   "processData": false,
#   "data": "{\n\t\"user_input\":\"onClick on div\"\n}"
# }

# $.ajax(settings).done(function (response) {
#   console.log(response);
# });