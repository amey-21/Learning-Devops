from flask import Flask, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')  # Load the MongoDB URI from the .env file

uri = MONGO_URI  # Ensure you have the correct MongoDB URI in your .env file

client = MongoClient(uri, server_api=ServerApi('1')) 

db = client.test
collection = db['flask_assignment'] 

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.get_json()
    collection.insert_one(form_data)

    return "Data Submitted Successfully"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 6000, debug=True)
