import json
import services.strava
from flask import Flask
from flask import render_template

with open('config.json') as json_data_file:
    jsonData = json.load(json_data_file)

clientId = jsonData['clientId']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/strava')
def stravaDashboard():
    return render_template('strava.html', clientId = clientId)

@app.route('/authorize/success')
def authorizeSuccess():
    athleteInfo = strava.GetAthleteInfo()
    athleteActivities = strava.GetAthleteAcitivites()

    return render_template('authorized.html', athleteInfo = athleteInfo, athleteActivities = athleteActivities)