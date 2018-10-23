from flask import Flask
import strava 
app = Flask(__name__)

@app.route('/authorize')
def authorize():

    'https://www.strava.com/oauth/authorize?client_id={}&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fauthorize%2Fsuccess&response_type=code&approval_prompt=auto&scope=read,activity:read'

    return 'Authorize'

@app.route('/authorize/success')
def authorizeSuccess():
    return 'Success'