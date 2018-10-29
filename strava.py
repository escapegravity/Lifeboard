import requests
import json

with open('config.json') as json_data_file:
    jsonData = json.load(json_data_file)

domain = jsonData['domain']
baseApiUrl = jsonData['baseApiUrl']
oauthUrl = jsonData['oauthUrl']
clientId = jsonData['clientId']
clientSecret = jsonData['clientSecret']
refreshToken = jsonData['refreshToken']

#code should be stored from when authorizing the application?
code = jsonData['code']

def GetToken(grantType):   
    response = requests.post('{}/{}'.format(domain, oauthUrl), data='client_id={}&client_secret={}&code={}&grant_type={}&refresh_token={}'.format(clientId, clientSecret, code, grantType, refreshToken))
    return response.json()['access_token']

def GetFromStravaAPI(endpoint):
    #Can't get activities when using refresh_token, only authorization_code
    access_token = GetToken("authorization_code") #refresh_token / authorization_code

    response = requests.get('{}{}/{}'.format(domain, baseApiUrl, endpoint), headers={'Authorization': 'Bearer {}'.format(access_token)})
    return response.json()

def GetAthleteInfo():
    return GetFromStravaAPI('athlete')

def GetAthleteAcitivites():
    return GetFromStravaAPI('athlete/activities')
    

#print(json.dumps(GetAthleteInfo(), indent=2))
#print(json.dumps(GetAthleteAcitivites(), indent=2))