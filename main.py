from flask import Flask
from flask import render_template
import json
from strava import GetAthleteInfo
from strava import GetAthleteAcitivites

with open('config.json') as json_data_file:
    jsonData = json.load(json_data_file)

clientId = jsonData['clientId']

app = Flask(__name__)

@app.route('/')
def authorize():
    return render_template('index.html', clientId = clientId)

@app.route('/authorize/success')
def authorizeSuccess():

    athleteInfo = GetAthleteInfo()
    athleteActivities = GetAthleteAcitivites()

    return render_template('authorized.html', athleteInfo = athleteInfo, athleteActivities = athleteActivities)