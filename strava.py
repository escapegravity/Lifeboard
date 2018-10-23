import requests
import json

domain = 'https://www.strava.com'
baseApiUrl = '/api/v3'

with open('config.json') as json_data_file:
    jsonData = json.load(json_data_file)

clientId = jsonData['clientId']
clientSecret = jsonData['clientSecret']
refreshToken = jsonData['refreshToken']

#code should be stored from when authorizing the application?
code = jsonData['code']

def RefreshToken():   
    #Can't get activities when using refresh_token, only authorization_code
    grant_type = 'authorization_code' #refresh_token / authorization_code

    response = requests.post('https://www.strava.com/oauth/token', data='client_id={}&client_secret={}&code={}&grant_type={}&refresh_token={}'.format(clientId, clientSecret, code, grant_type, refreshToken))
    return response.json()['access_token']

def GetFromStravaAPI(endpoint):
    access_token = RefreshToken()
    response = requests.get('{}{}/{}'.format(domain, baseApiUrl, endpoint), headers={'Authorization': 'Bearer {}'.format(access_token)})
    return response.json()

def GetAthleteInfo():
    return GetFromStravaAPI('athlete')

def GetAthleteAcitivites():
    return GetFromStravaAPI('athlete/activities')
    

print(json.dumps(GetAthleteInfo(), indent=2))
print(json.dumps(GetAthleteAcitivites(), indent=2))
