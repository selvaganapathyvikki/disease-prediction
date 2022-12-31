
from flask import Flask, render_template, request
import requests
import werkzeug

import pickle

app = Flask(__name__)

model = pickle.load(open('model.sav', 'rb'))

@app.route('/new', methods=["GET"])
def new():

    return "hew"

@app.route('/', methods=['GET'])
def hello() :
    
    return "helloo"


if __name__ == "__main__":
    app.run(debug=True)