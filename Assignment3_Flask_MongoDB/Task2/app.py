#Q2. Task-2: Frontend Form with MongoDB Atlas
from flask import Flask, request, render_template, jsonify, url_for
from dotenv import load_dotenv
import os
import pymongo
from pymongo.errors import ConnectionFailure, PyMongoError

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')


try:
    client = pymongo.MongoClient(MONGO_URI)
    db = client.test
    collection = db['flaskDB']

    client.server_info()

except (ConnectionFailure, PyMongoError):
    collection = None

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    if collection is None:
        return jsonify({"error": "DB connection failed."}), 503

    form_data = dict(request.form)

    if not form_data or not any(form_data.values()):
        return 'No data provided', 400


    try:
        collection.insert_one(form_data)
        return render_template('success.html'), 200

    except PyMongoError as e:
        return jsonify({"error":f"Failed to save data to DB: {str(e)}"}), 500
   

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/view')
def view():

    data = collection.find()

    data = list(data)

    for i in data:
        print(i)
        del i['_id']

    data = {
        'data':data
    }
    return data


if __name__=='__main__':
    app.run(debug=True)