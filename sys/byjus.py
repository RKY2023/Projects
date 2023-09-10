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
import pymysql as ps
from datetime import datetime
# print(br.response().read())
# https://byjusexamprep.com/batch/8586c342-08f5-11ee-9608-5dec56f8909c/batch-outline
subdivclass = ""
chapterdivclass = "ma0 deep-gray-vns body-6-d pl3 flex-grow-1"
topicdivclass = ""
code = "var sub=[]; var subid=[]; while ($('p.mb-1.ma0.pointer.deep-gray-vns.display-6-d') !=undefined) {    sub.push($('p.mb-1.ma0.pointer.deep-gray-vns.display-6-d').innerHTML);subid.push($('p.mb-1.ma0.pointer.deep-gray-vns.display-6-d').attributes['data-id'].textContent);$('p.mb-1.ma0.pointer.deep-gray-vns.display-6-d').remove();}"
sub = ['Demo Classes', 'Engineering Mathematics', 'Weekly Quiz', 'Complier Design', 'Digital Logic', 'Computer Organization', 'Computer Networks', 'Programming and Data Structures', 'Operating System', 'Algorithms', 'DBMS', 'Theory of Computation', 'Discrete Mathematics', 'General Aptitude', 'GATE Orientation Sessions', 'Test Series Schedule &amp; Syllabus', 'General Sessions']
subid = ['95b21576-0910-11ee-9a60-8d3143b788bd', '7ca67e5e-1708-11ee-8a61-07dcb4ad5ddd', '9f40a044-0910-11ee-b81f-59eb9ac9424f', '5defce02-14ab-11ee-83de-2598fce1c9bb', '985ecbb6-0910-11ee-827d-33fcb4b394a0', '998a7ce2-0910-11ee-81d6-b38d886f9a5c', '960d94e6-0910-11ee-ab8a-83785c170fd1', 'a7e6dc40-0910-11ee-9b57-e7baf3a5b73e', 'a85a7f38-0910-11ee-a3ab-4d5f0fe6b971', 'a94c9214-0910-11ee-bf43-5d80d966a62c', 'aa8996cc-0910-11ee-9b57-e7baf3a5b73e', 'ab4db8b8-0910-11ee-9f8f-43553c22b5cf', 'ad0381b0-0910-11ee-a3ab-4d5f0fe6b971', 'a91493dc-0910-11ee-9b57-e7baf3a5b73e', '8c07d314-11a1-11ee-b27f-eb31c8c8b960', '66c4bef2-1f23-11ee-b0ca-1b0096488096', '7bb92cda-2216-11ee-8157-cf536b3a7a7c']
# for s in sub:
#     os.mkdir('D:\\Learnings\\GATE\\GATE 2024\\'+s)

subid1 = pd.Series(subid) 
sub1 =  pd.Series(sub) 
subjects = pd.concat([ subid1, sub1], axis=1)
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

subjectUrls()

import time
import pyperclip
import pyautogui
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

def console_sv():
    code2 = '!function(e){e.save=function(o,n){if(o){n||(n="console.json"),"object"==typeof o&&(o=JSON.stringify(o,void 0,4));var t=new Blob([o],{type:"text/json"}),a=document.createEvent("MouseEvents"),s=document.createElement("a");s.download=n,s.href=window.URL.createObjectURL(t),s.dataset.downloadurl=["text/json",s.download,s.href].join(":"),a.initMouseEvent("click",!0,!1,window,0,0,0,0,0,!1,!1,!1,!1,0,null),s.dispatchEvent(a)}else e.error("Console.save: No data")}}(console);'
    pyautogui.write(code2)
    pyautogui.press("enter")
    time.sleep(1)

    autoGUI_clr_console()
    pyautogui.write('console.save(sub,)')
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.moveTo(1750, 1010,2)
    pyautogui.click()

    toggleconsole()
    toggleconsole()
    autoGUI_clr_console()
    time.sleep(1)
    pyautogui.write('console.save(subid,)')
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.moveTo(1750, 1010,2)
    pyautogui.click()
    toggleconsole()

def autoGUI(code):
    # for minimizing visual studio
    time.sleep(1)
    pyautogui.moveTo(1810, 20, 1)
    pyautogui.click()

    # byjus window
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(2)
    pyautogui.moveTo(200, 200, 1)
    pyautogui.click()
    
    # byjus console
    toggleconsole()
    time.sleep(1)

    autoGUI_clr_console()   
    time.sleep(1)

    pyautogui.write(code)
    pyautogui.press("enter")
    time.sleep(5)
    console_sv()
        
# autoGUI(code)
