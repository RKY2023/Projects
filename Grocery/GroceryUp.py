from __future__ import print_function

import os.path
import time
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

cred = credentials.Certificate("D:\\Livings\\Credentials\\Google\\firebase\\scheduler-m1-Key.json")
app =  firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://console.firebase.google.com/project/scheduler-m1/database/scheduler-m1-default-rtdb/data/~2F'
})
db = firestore.client()

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
        service = build('gmail', 'v1', credentials=creds)
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
        ts_before = str(int(time.time()))
        ts_after = str(int(time.time() - (604800*30))) # 1 month
        user = service.users()
        results = user.messages().list(userId='me',q='is:unread after:'+ts_after+' before:'+ts_before).execute()
        print(results)
        messages = results.get('messages', [])

        if not messages:
            print('No labels found.')
            return
        print('messages:')
        for message in messages:
            print(message['id'])
            messageid = message['id']
            # raw = service.users().messages().get(userId='me',id=message['id'],format='raw').execute()
            # t = base64.urlsafe_b64decode(raw['raw']).decode('utf-8')
            # print(t)
            msgId2cloudUp(user,messageid)
            
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

def movecontent2csv(filename, data):
    json_string = json.dumps(data)
    filename = 'D:\\Livings\\MailDump\\'+filename
    # print(json_string)
    with open(filename+'_json_data.json', 'w') as outfile:
        outfile.write(json_string)

def GroceryDataCSV(filename, data):
    json_string = json.dumps(data)
    filename = 'D:\\Livings\\MailDump\\Grocery\\'+filename
    # print(json_string)
    with open(filename+'_json_data.json', 'w') as outfile:
        outfile.write(json_string)

def msgId2cloudUp(user , msgid):
    full = user.messages().get(userId='me',id = msgid ,format='full').execute()
    header = full['payload']['headers']
    # snip = full['payload']['header']
    # print(snip)
    filename =''
    receiverName = ''
    subject = ''
    for names in header:
        if(names['name']=='From'):
            receiverName = names['value'].split('<')[0]
        if(names['name']=='Subject'):
            subject = names['value']
    subject = subject.replace('/','').replace('\\','').replace(':','').replace('?','').replace('*','').replace('"','').replace('<','').replace('>','').replace('|','')
    filename = msgid+'_'+receiverName+'_'+subject
    print(filename)
    
    movecontent2csv(filename, full)
    if(receiverName != 'alerts@bigbasket.com') :
        return
    # return # Uncomment if you want to dump all threads
    extractDataFromThread(msgid, full)

def extractDataFromThread(msgid, full):
    parts = full['payload']['parts']
    htmldata = ""
    for part in parts:
        htmldata = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
    
    doc = BeautifulSoup(htmldata, "html.parser")
    # doc = "".join(line.strip() for line in doc.split("\n"))
    table=doc.find('table')
    table=table.find('table')
    table=table.find('table')
    table=table.find('table')

    table=table.find_all('table')
    # print(table)
    # header = table.find
    # print(table[2].prettify())
    order_no = ''
    if(table[1].find_all('td')[0].text == 'Order No:'):
        order_no = table[1].find_all('td')[1].text
    delivery_slot = ''
    if(table[1].find_all('td')[2].text == 'Delivery slot:'):
        delivery_slot = table[1].find_all('td')[3].text
    headers = []
    # td_list = table[2].find_all('tr')[0]
    # if(table[2].find_all('tr')[0].text == 'Delivery slot:'):
    #     delivery_slot = table[1].find_all('td')[3].text

    for td in table[2].find('tr').find_all("td"):
        headers.append(td)
    #print(row)

    # headers.pop(0)

    # df = pd.DataFrame(headers, columns=['PostalCode', 'Borough', 'Neighborhood'])
    header = pd.DataFrame(headers)
    # print(header)
    data = []
    break_flag=0
    for tr in table[2].find_all('tr'):
        break_flag+=1
        if(break_flag==1):
            continue
        row=[]
        tr_txt = "".join(line.strip() for line in tr.text.split("\n"))
        if(tr_txt.find('total value')>1):
            break
        td = tr.find_all("td")
        for t in td:
            t = "".join(line.strip() for line in t.text.split("\n"))
            if(t==""):
                continue
            row.append(t)
        data.append(np.array(row))
    df = pd.DataFrame(data)
    print(df)
    kk =  df.to_dict('records')
    for k in kk:
        dataaa = {
            "Original_Qty": k[0],
            "Original_Value_(Rs)": k[1],
            "Revised_Item": k[2],
            "Revised_Qty": k[3],
            "Revised_Value_(Rs)": k[4]
        }
        db.collection('Grocery').document(k[0]).set(dataaa)

    # Dump htmldata
    # print(htmldata)
    with open('D:\\Livings\\MailDump\\Grocery\\htmlData'+msgid+'.html', 'w') as outfile:
        outfile.write(htmldata)
    

    # dump dict to sample.json
    df2 = df.to_json(orient = 'table')
    GroceryDataCSV(msgid, df2)
    # exit()
    
    # f = open("msgD.html", "a")
    # f.write(rs)
    # f.close()



if __name__ == '__main__':
    main()