#Q1. Task-1: JSON API Route
from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

BK_FILE = os.path.join(DIR_PATH, 'data.json')

@app.route('/')
def home():
    return ' Welcome to the HomePage '


@app.route('/api')
def get_json_data():
    try:
        with open(BK_FILE, 'r') as file:
            file_data = json.load(file)

        return jsonify(file_data), 200

    except FileNotFoundError:

        return jsonify({"error":"File Missing"}), 404
    

if __name__=='__main__':
    app.run(debug=True)