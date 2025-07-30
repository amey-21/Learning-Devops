from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def home():

    data = json.load(open('text.json')) 
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

