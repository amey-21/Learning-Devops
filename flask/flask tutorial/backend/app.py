from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI') # Load the MongoDB URI from the .env file

uri = MONGO_URI # Ensure you have the correct MongoDB URI in your .env file

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1')) # Ensure you have the correct MongoDB URI

db = client.test # Replace 'test' with your database name
collection = db['flask_tutorial'] # Ensure the collection exists

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.json) # Get form data as a dictionary
    collection.insert_one(form_data) # Insert the form data into the MongoDB collection

    return "Data Submitted Successfully" # You can redirect to another page or render a template here

@app.route('/view')
def view():
    data = collection.find() # Retrieve all documents from the collection
    data = list(data) # Convert the cursor to a list for easier manipulation
    for items in data:
        print(items)
        del items['_id'] # Remove the MongoDB ObjectId from the output

    return jsonify(data) # Return the data as JSON

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 9000, debug=True)


