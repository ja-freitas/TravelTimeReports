from flask import Flask, render_template, request
import sqlite3, requests, json, doctest

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input', methods=['GET'])
def input():
    """Accepts user input for Google API
    >>> input()
    'Response Status 200'"""

    origin = request.args['origin']
    destination = request.args['destination']

    response = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&departure_time=now&key=AIzaSyAZEe218wR5BpZMdLHZEpub0Ym8ccP1QNM' % (origin, destination))

    if response.status_code == 200:
        return 'Response Status %d' % response.status_code))
    else:
        return status_codes
