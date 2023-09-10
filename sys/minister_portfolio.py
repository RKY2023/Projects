from bs4 import BeautifulSoup
import requests
import time
import datetime
from datetime import datetime as dt



def checkAndUpdate():
    url_link = "https://www.india.gov.in/my-government/whos-who/council-ministers"
    result = requests.get(url_link).text
    doc = BeautifulSoup(result, "html.parser")
    com=doc.findAll('section', class_='pane-union-council-of-ministers')
    # cabinetMinisters=doc.findAll('div', class_='view-union-council-of-ministers')
    # print(cabinetMinisters)
    # cabinetMinisters.findAll('td')
    for m in com:
        # print(m)
        t= m.find('h2')
        print(t)
        if(t.text == 'Cabinet Ministers'):
            for m2 in m:
                # print(m2)
                mtt = m.find('div', class_='view-union-council-of-ministers')
                trr = mtt.findAll('td')
                print(trr)
                for m3 in trr:
                    imgdiv = m3.find('div', class_='views-field-field-image')
                    # img = m3.find('img')
                    # img=img.src
                    # print(img)
                    name = m3.find('div', class_='views-field-title')
                    name = name.text
                    print(name)
                    portfolios = m3.find('div', class_='views-field-field-ministries')
                    portfolios = portfolios.findAll('li')
                    for p in portfolios:
                        p = p.text
                        p = p.replace('Ministry of ', '')
                        print(p)

checkAndUpdate()

# def data2Json():
#     a 
