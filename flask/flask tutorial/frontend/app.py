from flask import Flask, render_template, request
from datetime import datetime
import requests

BACKEND_URL = 'http://localhost:9000'  # URL of the backend Flask app

app = Flask(__name__)

@app.route('/')

def home():
    day_of_week = datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)  # Send form data to the backend
    return "Data Submitted Successfully"  # You can redirect to another page or render a template here

@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL + '/view')

    return response.json()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug=True)


