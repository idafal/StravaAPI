import json
import requests
import time
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
    print(strava_tokens)
    # Save tokens to file
    with open(filename, 'w') as outfile:
        json.dump(strava_tokens, outfile)
    return strava_tokens

def stravaAuthAPIcall_automaticRefresh(clientId, clientSecret, filename):
    """

    :param clientId:
    :param clientSecret:
    :param urlCode:
    :param filename:
    :return:
    """

    print("Loading old tokens")
    with open('strava_tokens.json') as json_file:
        strava_tokens = json.load(json_file)

    # use the refresh_token to get the new access_token

    if strava_tokens['expires_at'] < time.time():
        print("Token has expired. \nLoading new tokens")
        # Make Strava auth API call with current refresh token
        response = requests.post(
            url='https://www.strava.com/oauth/token',
            data={
                'client_id': clientId,
                'client_secret': clientSecret,
                'grant_type': 'refresh_token',
                'refresh_token': strava_tokens['refresh_token']
            }
        )
        # Save response as json in new variable
        new_strava_tokens = response.json()
        # Save new tokens to file
        with open(filename, 'w') as outfile:
            json.dump(new_strava_tokens, outfile)
        # Use new Strava tokens from now
        strava_tokens = new_strava_tokens

    return strava_tokens

def read_tokens(filename):
    with open(filename) as check:
        tokens = json.load(check)
    return tokens['access_token']
