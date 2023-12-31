# import mechanize
# from bs4 import BeautifulSoup
# import urllib
# import http.cookiejar ## http.cookiejar in python3

# cj = http.cookiejar.CookieJar()
# br = mechanize.Browser()
# br.set_cookiejar(cj)
# br.open("https://id.arduino.cc/auth/login/")

# br.select_form(nr=0)
# br.form['username'] = 'VioletSloth680'
# br.form['password'] = 'kQbQ7qX3gy@nib.'
# br.submit()

import os
import json
import pandas as pd
from pandas import json_normalize
import pymysql as ps
from datetime import datetime
import time
import pyperclip
import pyautogui
# print(br.response().read())
# https://byjusexamprep.com/batch/8586c342-08f5-11ee-9608-5dec56f8909c/batch-outline
array = [['subject','mb-1 ma0 pointer deep-gray-vns display-6-d'],['chapter','ma0 deep-gray-vns body-6-d pl3 flex-grow-1'],['topic','ma0 deep-gray-vns body-6-d pl3 flex-grow-1']]
sub = ['Demo Classes', 'Engineering Mathematics', 'Weekly Quiz', 'Complier Design', 'Digital Logic', 'Computer Organization', 'Computer Networks', 'Programming and Data Structures', 'Operating System', 'Algorithms', 'DBMS', 'Theory of Computation', 'Discrete Mathematics', 'General Aptitude', 'GATE Orientation Sessions', 'Test Series Schedule &amp; Syllabus', 'General Sessions']
subid = ['95b21576-0910-11ee-9a60-8d3143b788bd', '7ca67e5e-1708-11ee-8a61-07dcb4ad5ddd', '9f40a044-0910-11ee-b81f-59eb9ac9424f', '5defce02-14ab-11ee-83de-2598fce1c9bb', '985ecbb6-0910-11ee-827d-33fcb4b394a0', '998a7ce2-0910-11ee-81d6-b38d886f9a5c', '960d94e6-0910-11ee-ab8a-83785c170fd1', 'a7e6dc40-0910-11ee-9b57-e7baf3a5b73e', 'a85a7f38-0910-11ee-a3ab-4d5f0fe6b971', 'a94c9214-0910-11ee-bf43-5d80d966a62c', 'aa8996cc-0910-11ee-9b57-e7baf3a5b73e', 'ab4db8b8-0910-11ee-9f8f-43553c22b5cf', 'ad0381b0-0910-11ee-a3ab-4d5f0fe6b971', 'a91493dc-0910-11ee-9b57-e7baf3a5b73e', '8c07d314-11a1-11ee-b27f-eb31c8c8b960', '66c4bef2-1f23-11ee-b0ca-1b0096488096', '7bb92cda-2216-11ee-8157-cf536b3a7a7c']
pageURLchanged=0
firstrun = True
location = 'D:\\'
# for s in sub:
#     os.mkdir('D:\\Learnings\\GATE\\GATE 2024\\'+s)
subjects = []
chapters = []
topics = []
all_URL = []
# print(subjects)
def insertSubjects():
    try:
        cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='sys')
        cmd=cn.cursor()
        # sql = "CREATE TABLE `sys`.`byju2024topics` (  `id` VARCHAR(100) NOT NULL,  `topic` VARCHAR(100) NULL,  PRIMARY KEY (`id`));"
      
        for i,row in subjects.iterrows():
            sql = "INSERT INTO sys.byju2024subjects(id,subject) VALUES (%s,%s)"
            cmd.execute(sql, tuple(row))
            print("Record inserted")
            cn.commit()
        
        cn.close()

    except Exception as e:
        print(e)

def insertChapters():
    try:
        cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='sys')
        cmd=cn.cursor()
        # sql = "CREATE TABLE `sys`.`byju2024topics` (  `id` VARCHAR(100) NOT NULL,  `topic` VARCHAR(100) NULL,  PRIMARY KEY (`id`));"
      
        for i,row in subjects.iterrows():
            sql = "INSERT INTO sys.byju2024subjects(id,subject) VALUES (%s,%s)"
            cmd.execute(sql, tuple(row))
            print("Record inserted")
            cn.commit()
        
        cn.close()

    except Exception as e:
        print(e)

def subjectUrls():
    try:
        cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='sys')
        cmd=cn.cursor()
        # sql = "CREATE TABLE `sys`.`byju2024topics` (  `id` VARCHAR(100) NOT NULL,  `topic` VARCHAR(100) NULL,  PRIMARY KEY (`id`));"
      
        sql = "SELECT id FROM sys.byju2024subjects"
        tuplescount = cmd.execute(sql)
        tuples = cmd.fetchall()
        print("Record Found:",tuplescount)
        for row in tuples:
            print('https://byjusexamprep.com/batch/8586c342-08f5-11ee-9608-5dec56f8909c/batch-outline?subjectId='+str(row[0]))
            cn.commit()
        
        cn.close()

    except Exception as e:
        print(e)

def toggleconsole():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown("shift")
    pyautogui.press("j")
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp("shift")

def autoGUI_clr_console():
    # byjus console clear 
    pyautogui.keyDown('ctrl')
    pyautogui.press("l")
    pyautogui.keyUp('ctrl')

def rightclk():
    # byjus console clear 
    pyautogui.keyDown('shift')
    pyautogui.press("f10")
    pyautogui.keyUp('shift')

def console_sv(filename):
    code2 = '!function(e){e.save=function(o,n){if(o){n||(n="console.json"),"object"==typeof o&&(o=JSON.stringify(o,void 0,4));var t=new Blob([o],{type:"text/json"}),a=document.createEvent("MouseEvents"),s=document.createElement("a");s.download=n,s.href=window.URL.createObjectURL(t),s.dataset.downloadurl=["text/json",s.download,s.href].join(":"),a.initMouseEvent("click",!0,!1,window,0,0,0,0,0,!1,!1,!1,!1,0,null),s.dispatchEvent(a)}else e.error("Console.save: No data")}}(console);'
    pyautogui.write(code2)
    pyautogui.press("enter")
    time.sleep(1)

    for i, fn in enumerate(filename):
        if(i!=0):
            toggleconsole()
            toggleconsole()
        time.sleep(1)
        autoGUI_clr_console()
        if(i!=0):
            time.sleep(1)
        pyautogui.write('console.save('+filename[i]+',)')
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.moveTo(1750, 1010,2)
        pyautogui.keyDown("alt")
        pyautogui.press("n")
        pyautogui.keyUp("alt")
        pyautogui.write(filename[i])
        pyautogui.moveTo(1750, 1010,2)
        pyautogui.click()

    toggleconsole()

def autoGUI(code,entity,url):
    global pageURLchanged, firstrun
    if(pageURLchanged ==0 or firstrun):
        # for minimizing visual studio
        time.sleep(1)
        print('Starting AutoGUI...')
        pyautogui.moveTo(1810, 20, 1)
        pyautogui.click()
        print(pageURLchanged)
    # byjus window
    time.sleep(1)
    if(pageURLchanged ==0 or firstrun):
        pyautogui.press('f5')
        time.sleep(2)
        firstrun = False
    elif(pageURLchanged !=0):
        pyautogui.keyDown('ctrl')
        pyautogui.press('l')
        pyautogui.keyUp('ctrl')
        pyautogui.write(url)
        pyautogui.press('enter')
        time.sleep(5)
    pyautogui.moveTo(200, 200, 1)
    # exit()
    pyautogui.click()
    
    
    # byjus console
    toggleconsole()
    time.sleep(1)

    autoGUI_clr_console()   
    time.sleep(1)
    # exit()
    pyautogui.write(code)
    pyautogui.press("enter")
    time.sleep(5)
    file_names = [entity+'_name',entity+'_id']
    console_sv(file_names)
    convertCSV(file_names[0],file_names[1])

def upsert_Subject_Chapter_Topic():
    global pageURLchanged
    # jsListCode = "var list = document.getElementsByClassName('ma0 deep-gray-vns body-6-d pl3 flex-grow-1')"
    # file_names = ['list']
    # console_sv(file_names)
    # exit()
    for i in array:
        # if(pageURLchanged == 0):  
        #     print(i[0], i[1])
        #     code = "var list = document.getElementsByClassName('"+i[1]+"'); var "+i[0]+"_name=[]; var "+i[0]+"_id=[]; for (let index = 0; index < list.length; index++) {"+i[0]+"_name.push(list[index].innerHTML); "+i[0]+"_id.push(list[index].attributes['data-id'].textContent);}"
        #     autoGUI(code,i[0],'')
            
        if(pageURLchanged == 1):        
            print(i[0], i[1])
            code = "var list = document.getElementsByClassName('"+i[1]+"'); var "+i[0]+"_name=[]; var "+i[0]+"_id=[]; for (let index = 0; index < list.length; index++) {"+i[0]+"_name.push(list[index].innerHTML); "+i[0]+"_id.push(0);}"
            df = pd.read_csv('D:\Byjus_subject_name.csv')
            df['url'] = 'https://byjusexamprep.com/batch/8586c342-08f5-11ee-9608-5dec56f8909c/batch-outline?subjectId=' +df['subject_id'].map(str)
            for url in df['url'].to_numpy():
                print(url)
                autoGUI(code,i[0],url)
                exit()
            
        pageURLchanged +=1

def convertCSV(file_name, file_id):
    f1 = open(location+file_name+'.json')
    f2 = open(location+file_id+'.json')
    data1 = f1.read().replace('[','').replace(']','').replace('\n','').replace('    ','')
    data1 = data1[1:len(data1)-1]
    data1 = data1.split('","')
    data2 = f2.read().replace('[','').replace(']','').replace('\n','').replace('    ','')
    data2 = data2[1:len(data2)-1]
    data2 = data2.split('","')
    f1.close()
    f2.close()
    df1 = pd.Series(data1)
    df2 = pd.Series(data2)
    df = pd.concat([df1,df2], axis=1,keys=[file_name,file_id])
    print(df)
    isExistCSV = os.path.exists(location+file_name+'.csv')
    if(file_name == 'chapter_name' and isExistCSV):
        df_old = pd.read_csv(location+file_name+'.csv')
        df = pd.concat([df_old,df])
    df.to_csv('D:\Byjus_'+file_name+'.csv', index=False)  

def moveANDclick(x,y,doClick):
    pyautogui.moveTo(x, y, 1)
    if(doClick == 1):
        pyautogui.click()
    time.sleep(1)

def listcount():
    code = "var list = document.getElementsByClassName('ma0 deep-gray-vns body-6-d pl3 flex-grow-1'); var elem=[]; for (let index = 0; index < list.length; index++) {elem.push(list[index].innerHTML);}"
    toggleconsole()
    time.sleep(1)
    autoGUI_clr_console()   
    time.sleep(1)
    # exit()
    pyautogui.write(code)
    pyautogui.press("enter")
    time.sleep(1)
    file_names = ['elem']
    console_sv(file_names)
    time.sleep(1)
    toggleconsole()
    toggleconsole()
    f1 = open(location+file_names[0]+'.json')
    data1 = f1.read().replace('[','').replace(']','').replace('\n','').replace('    ','')
    data1 = data1[1:len(data1)-1]
    data1 = data1.split('","')
    print(data1)
    # exit()
    f1.close()
    os.remove(location+file_names[0]+'.json')
    return data1

def browserUrl(url):
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')
    pyautogui.write(url)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(200, 200, 1)
    pyautogui.click()

def  goBackBrowser():
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.press('left')
    pyautogui.keyUp('alt')
    time.sleep(1)

def autoGUILinks(url,res_sub):
    # byjus window
    browserUrl(url)

    domain_url = 'https://byjusexamprep.com/batch/8586c342-08f5-11ee-9608-5dec56f8909c/batch-outline?'
    
    # Traversing List starts
    # subject
    # moveANDclick(425,380,1) # 20px gap
    # moveANDclick(425,420)
    # chapter
    res_chapter = listcount()
    print(len(res_chapter))
    for i,res_ch in enumerate(res_chapter):
        moveANDclick(725,400+(i*60),1) # 40 px gap but 60 real

    # topic
        res_topic = listcount()
        print(len(res_topic))
        for j,res_top in enumerate(res_topic):
            moveANDclick(725,400+(j*60),1) # 40 px gap but 60 real
    # get URL & append
            pyautogui.keyDown('ctrl')
            pyautogui.press('l')
            pyautogui.keyUp('ctrl')
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')
            t = pyperclip.paste()
            subjects.append(res_sub)
            chapters.append(res_ch)
            topics.append(res_top)
            all_URL.append(t)
            moveANDclick(200,200,1)
            # tt = t.replace(domain_url,'')
            # tt = tt.split('&')
            # # go to subject page
            # print(domain_url+tt[0])
            # browserUrl(domain_url+tt[0])
            goBackBrowser()

        goBackBrowser()
    # print(all_URL)
    

def upsert_all_url():
    # for minimizing visual studio
    time.sleep(1)
    print('Starting AutoGUI...')
    pyautogui.moveTo(1810, 20, 1)
    pyautogui.click()

    df = pd.read_csv('D:\Byjus_subject_name.csv')
    df['url'] = 'https://byjusexamprep.com/batch/8586c342-08f5-11ee-9608-5dec56f8909c/batch-outline?subjectId=' +df['subject_id'].map(str)
    for url in df.to_numpy():
        print(url[3],url[2])
        autoGUILinks(url[3],url[2]) 
    
    sub_DF = pd.DataFrame(subjects)
    ch_DF = pd.DataFrame(chapters)
    top_DF = pd.DataFrame(topics)
    url_DF = pd.DataFrame(all_URL)
    
    MainDataFrame = pd.concat([sub_DF, ch_DF, top_DF, url_DF], axis=1)
    MainDataFrame.columns =['subject', 'chapter', 'topic', 'url']
    print(MainDataFrame)
    MainDataFrame.to_csv('D:\\BYJUS_All.csv',index=False)  
# subjectUrls()
# upsert_Subject_Chapter_Topic()

upsert_all_url()
# autoGUI(code)
# convertCSV()

