# https://data.gov.in/api

url = 'https://api.data.gov.in/resource/8d3b6596-b09e-4077-aebf-425193185a5b?api-key=579b464db66ec23bdd0000011f7181905bf546384569a2eee2ff0098&format=json'
# URLS 
# https://data.gov.in/resource/all-india-pincode-directory


from bs4 import BeautifulSoup
import requests
import time
import datetime
from datetime import datetime as dt
import os
import shutil

import platform
systemOS = platform.system()
print("Current OS: ", systemOS)
if(systemOS == 'Windows'):
    dirSeparator = '\\'
else:
    dirSeparator = '/'
dirname = os.path.dirname(__file__)

printFolder = True
api = 'https://api.data.gov.in/lists?format=json&notfilters[source]=visualize.data.gov.in&filters[active]=1&limit=8&offset=0&sort[created]=desc&filters[source][]=data.gov.in'
response = requests.get(api)
 
# Store JSON data in API_Data
API_Data = response.json()
# # Print json data using loop
# for key in API_Data:{
#     print(key,":", API_Data[key])
# }
records = API_Data['records']
for k in (records):
    for t in k:
        if(t=='title'):
            print(t['title']) 
    