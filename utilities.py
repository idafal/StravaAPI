import json
import requests
from pandas import json_normalize

def stravaAuthAPIcall(clientId, clientSecret, urlCode, filename):
    """
    Retrieve access and refresh tokens, write to file
    """
    response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': clientId,
            'client_secret': clientSecret,
            'code': urlCode,
            'grant_type': 'authorization_code'
        }
    )
    strava_tokens = response.json()
    # Save tokens to file
    with open(filename, 'w') as outfile:
        json.dump(strava_tokens, outfile)
    return strava_tokens

def read_tokens(filename):
    with open(filename) as check:
        tokens = json.load(check)
    return tokens['access_token']
