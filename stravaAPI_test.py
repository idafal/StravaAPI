import numpy as np
import json
import requests
from pandas import json_normalize
import csv


#  Client ID: 63053
#  Code: 638af175a5bcd1056d5c55d62f86e2f46907aada
clientId = 63053
clientSecret = '5277338dadfec5ab60cd7d750c40e59b5d36ffbe'
urlCode = 'fab591cf80699c88840ea2beba559f1ed9f0d487'  #  temporary

def stravaAuthAPIcall():
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
    with open('strava_tokens.json', 'w') as outfile:
        json.dump(strava_tokens, outfile)
    return strava_tokens

def read_tokens():
    with open('strava_tokens.json') as check:
        tokens = json.load(check)
    return tokens


def read_activities():
    """
    Save first page of activities to csv for inspection
    :return:
    """
    strava_tokens = read_tokens()
    # Loop through all activities
    url = "https://www.strava.com/api/v3/activities"
    access_token = strava_tokens['access_token']
    # Get first page of activities from Strava with all fields
    r = requests.get(url + '?access_token=' + access_token)
    r = r.json()
    df = json_normalize(r)
    df.to_csv('strava_activities_all_fields.csv')

    return