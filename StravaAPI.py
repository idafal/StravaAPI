import pandas as pd
import utilities as util
import requests
import time

#  Client ID: 63053
#  Code: 638af175a5bcd1056d5c55d62f86e2f46907aada

filename = 'strava_tokens.json'
clientId = 63053
clientSecret = '5277338dadfec5ab60cd7d750c40e59b5d36ffbe'
urlCode = 'f2172a4761f062755910c273c4779a1e9b490034'  #  temporary - found by inserting url in webbrowser

def read_all_activities():
    #  Get token
    util.stravaAuthAPIcall_automaticRefresh(clientId, clientSecret, filename)
    access_token = util.read_tokens(filename)
    # Create dataframe with relevant data
    activities = pd.DataFrame(
        columns=[
            "id",
            "name",
            "start_date_local",
            "type",
            "distance",
            "moving_time",
            "total_elevation_gain",
           # "start_latlng",
            #"end_latlng",
            "achievement_count",
            "athletes_count",
            "commute",
            "average_speed",
            "max_speed",
            #"average_cadence",
            "external_id"
           # "elev_high",
          #  "elev_low"
        ]
    )

    page = 1
    url = "https://www.strava.com/api/v3/activities"

    while True:

        # get page of activities from Strava
        r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
        r = r.json()

        # if no results then exit loop
        if (not r):
            break
        # print(f"r:\n",r)
        # print(f"r",r[0])

        # otherwise add new data to dataframe
        for x in range(len(r)):
            activities.loc[x + (page - 1) * 200, 'id'] = r[x]['id']
            activities.loc[x + (page - 1) * 200, 'name'] = r[x]['name']
            activities.loc[x + (page - 1) * 200, 'start_date_local'] = r[x]['start_date_local']
            activities.loc[x + (page - 1) * 200, 'type'] = r[x]['type']
            activities.loc[x + (page - 1) * 200, 'distance'] = r[x]['distance']
            activities.loc[x + (page - 1) * 200, 'moving_time'] = r[x]['moving_time']

            activities.loc[x + (page - 1) * 200, 'total_elevation_gain'] = r[x]['total_elevation_gain']
           # activities.loc[x + (page - 1) * 200, 'start_latlng'] = r[x]['start_latlng']
            #activities.loc[x + (page - 1) * 200, 'end_latlng'] = r[x]['end_latlng']
            activities.loc[x + (page - 1) * 200, 'achievement_count'] = r[x]['achievement_count']
            activities.loc[x + (page - 1) * 200, 'athlete_count'] = r[x]['athlete_count']
            activities.loc[x + (page - 1) * 200, 'commute'] = r[x]['commute']
            activities.loc[x + (page - 1) * 200, 'average_speed'] = r[x]['average_speed']
            activities.loc[x + (page - 1) * 200, 'max_speed'] = r[x]['max_speed']
           # activities.loc[x + (page - 1) * 200, 'average_cadence'] = r[x]['average_cadence']
            activities.loc[x + (page - 1) * 200, 'external_id'] = r[x]['external_id']
           # activities.loc[x + (page - 1) * 200, 'elev_high'] = r[x]['elev_high']
           # activities.loc[x + (page - 1) * 200, 'elev_low'] = r[x]['elev_low']
        # increment page
        page += 1
    activities.to_csv('strava_activities.csv')
    print("Activities successfully written to strava_activities.csv")
    return

def testapicall():
    print("test")
    util.stravaAuthAPIcall_automaticRefresh(clientId, clientSecret, filename)
    access_token = util.read_tokens(filename)

    return