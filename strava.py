import requests
import json

domain = 'https://www.strava.com'
baseApiUrl = '/api/v3'

def RefreshToken(): 
    clientId = '29492'
    clientSecret = 'af5bdd207222b44859bd7172c036f0f6a1cc8b17'
    refreshToken = 'c071f4869ae855c1b329adc9a6a49bb5f37aec90 '

    response = requests.post('https://www.strava.com/oauth/token', data='client_id={}&client_secret={}&grant_type=refresh_token&refresh_token={}'.format(clientId, clientSecret, refreshToken))

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
