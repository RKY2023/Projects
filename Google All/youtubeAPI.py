from __future__ import print_function

import os.path

import json
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


# help('modules')
# python3 -m venv install google-api-python-client google-auth-httplib2 google-auth-oauthlib google
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# cred = credentials.Certificate("D:\\Livings\\Credentials\\Google\\firebase\\scheduler-m1-Key.json")
# app =  firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://console.firebase.google.com/project/scheduler-m1/database/scheduler-m1-default-rtdb/data/~2F'
# })
# db = firestore.client()
# anime = ['one-piece','kimetsu-no-yaiba-katanakaji-no-sato-hen']
# # ts = time.time()

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'D:\\Livings\\Credentials\\Google\\Gmail_rky\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('youtube', 'v3', credentials=creds)
        # results = service.users().getProfile(userId='me').execute()
        # results = service.users().labels().list(userId='me').execute()
        # labels = results.get('labels', [])

        # if not labels:
        #     print('No labels found.')
        #     return
        # print('Labels:')
        # for label in labels:
        #     print(label['name'])
        # https://developers.google.com/gmail/api/reference/quota

        # https://developers.google.com/gmail/api/guides/filtering


        user = service.videos()
        print(user.list(
        part="snippet",
        id="KZyBjyRlbHU"
    ).execute())
        # results = user.messages().list(userId='me',q='is:unread after:1685451000 before:1685451301').execute()
        # print(results)
        # messages = results.get('messages', [])

        # if not messages:
        #     print('No labels found.')
        #     return
        # print('messages:')
        # for message in messages:
        #     print(message['id'])
        #     messageid = message['id']
        #     # raw = service.users().messages().get(userId='me',id=message['id'],format='raw').execute()
        #     # t = base64.urlsafe_b64decode(raw['raw']).decode('utf-8')
        #     # print(t)
        #     msgId2cloudUp(user,messageid)
            
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')



if __name__ == '__main__':
    main()