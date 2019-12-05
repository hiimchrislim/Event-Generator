from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import requests

"""Authenticaion below"""
try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')

creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
        if flags else tools.run(flow, store)
CAL = build('calendar', 'v3', http=creds.authorize(Http()), developerKey='')

response = requests.get('http://localhost:5000/events/')
print(response.status_code)
# print(response.json())

for event in response.json():
    if event['end_year'] != 1:
        start_date = '%s-%s-%s' % (event['start_year'], event['start_month'], event['start_day'])
        end_date = '%s-%s-%s' % (event['end_year'], event['end_month'], event['end_day'])
        # 2019-08-25
        EVENT = {
            'description': "Important Date",
            'summary': event['info'],
            'start': {'date': start_date,
                      'timeZone': "EST"},
            'end': {'date': end_date,
                    'timeZone': "EST"},

        }
    else:
        start_date = "%s-%s-%s" % (event['start_year'], event['start_month'], event['start_day'])
        EVENT = {
            'description': "Important Date",
            'summary': event['info'],
            'start': {'date': start_date,
                      'timeZone': "EST"},
            'end': {'date': start_date,
                    'timeZone': "EST"},
        }
    e = CAL.events().insert(calendarId='primary', sendNotifications=False, body=EVENT).execute()
