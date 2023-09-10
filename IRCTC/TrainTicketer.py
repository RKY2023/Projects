import os
import time
import pyautogui
import os
import re
import shutil
from datetime import datetime
import pymysql as ps
# time.sleep(3)
passengerList = [
    ['Santosh kr', '25', 'm', 'n'],
    ['Jyoti Yadav', '28', 'f', 'v']
    ]
passengercount = len(passengerList)
ticket_class = 'AC3'
# t = time.localtime()
# hr = time.strftime("%H", t)
# if(hr == '11'):
#     ticket_class="SL"
# for i in passengerList:
#     detail_len = len(i)
#     print(detail_len)
#     for j in i:
#         print(j)
#         detail_len-=1
#         # print("s",idx)
#     print("\n")
def selectCoach():
    # for selecting ac coach
    pyautogui.moveTo(10, 10, 1)
    # time.sleep(1)
    # select AC 3
    pyautogui.moveTo(570, 550, 1)
    pyautogui.click()
    time.sleep(1)
    # click "Book Now"
    pyautogui.moveTo(550, 675, 1)
    pyautogui.click()

def passengerDetails_auto():
    for i in passengerList:
        if (len(passengerList) != passengercount):
            pyautogui.press('enter')
        detail_len = len(i)
        for passenger_detail in i:
            pyautogui.write(passenger_detail)
            if (len(passengerList) != passengercount and detail_len == 4):
                time.sleep(1)
            pyautogui.press('tab')
            if (detail_len==2):
                pyautogui.press('tab',presses=3)
            if (ticket_class == 'AC3'):
                pyautogui.write(passenger_detail)
                pyautogui.press('tab')
            detail_len-=1
        passengercount-=1
def passengerDetails_manual():
    pyautogui.write('Santosh kumar')
    pyautogui.press('tab')
    pyautogui.write('26')
    pyautogui.press('tab')
    pyautogui.press('m')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    if (ticket_class == 'AC3'):
        # pyautogui.press('n')
        pyautogui.press('n',presses=2)
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('Jyoti Yd')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write('29')
    pyautogui.press('tab')
    pyautogui.press('f')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    if (ticket_class == 'AC3'):
        pyautogui.press('n',presses=2)
        # pyautogui.press('v')
        pyautogui.press('tab')

def passengerDetails():
    # After "Book Now" -> Passenger details & UPI
    pyautogui.moveTo(10, 150, 1)
    pyautogui.click()
    pyautogui.scroll(1500)
    pyautogui.moveTo(50, 650, 1)
    pyautogui.click()
    # passengerDetails_auto()
    passengerDetails_manual()
    i=6
    while(i>0):    
        pyautogui.press('tab')
        i=i-1
    # Tick "Auto upgradation"
    # pyautogui.press('space')
    time.sleep(1)
    i=7
    while(i>0):    
        pyautogui.press('tab')
        i=i-1
    pyautogui.press('down')
    pyautogui.press('tab',presses=2)
    pyautogui.press('enter')
passengerDetails()

def ReviewJourney():
    # Review Journey
    mxReview=700
    myReview=750
    pyautogui.moveTo(mxReview, myReview, 1)
    pyautogui.moveTo(140, 820, 1)
    pyautogui.click()

def paymentMethod():
    #Pay Methods UPI
    mxPM=50
    myPM=480
    pyautogui.moveTo(mxPM, myPM, 1)
    pyautogui.click()
    pyautogui.moveTo(mxPM+550,myPM-90, 1)
    pyautogui.click()
    pyautogui.moveTo(mxPM+750,myPM+50, 1)
    pyautogui.click()

def updateStage(stg):
    try:
    #     CREATE TABLE `dota2`.`irctc` (
    #   `id` INT NOT NULL,
    #   `stage` INT NULL,
    #   PRIMARY KEY (`id`));

        cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='dota2')
        cmd=cn.cursor()
        stg+=1
        # sql = "INSERT INTO dota2.irctc(id, stage) VALUES (2,0)"
        sql = "UPDATE dota2.irctc SET stage="+str(stg)+" WHERE ID=1"
        cmd.execute(sql)
        # the connection is not auto committed by default, so we must commit to save our changes
        cn.commit()
        cn.close()

    except Exception as e:
        print(e)
    return stg

# print(updateStage(2))

# time.sleep(1)
# pyautogui.scroll(500)
# pyautogui.scroll(10, x=100, y=100) 
# pyautogui.click()
# time.sleep(1)
# # # scroll list //45px per item
# pyautogui.moveTo(915, 375, 1)
# time.sleep(1)
# pyautogui.press('f12')
# time.sleep(1)
# pyautogui.dragTo(915, 507, 2, button='left')
# time.sleep(2)
# pyautogui.press('f12')
# time.sleep(1)
# pyautogui.dragTo(915, 640, 2, button='left')
# time.sleep(2)
# pyautogui.press('f12')
# time.sleep(1)
# pyautogui.dragTo(915, 773, 2, button='left')
# time.sleep(2)
# pyautogui.press('f12')
# time.sleep(1)
# pyautogui.dragTo(915, 915, 2, button='left')
# time.sleep(2)
# pyautogui.press('f12')
# time.sleep(1)
# pyautogui.moveTo(1895, 30, 1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(855, 580, 1)
# pyautogui.click()
# time.sleep(1)

# # Move Screenshot to Work dir
# now = datetime.now()
# dt_string = now.strftime("%Y%m%d%H")
# files_and_directories = os.listdir("C:\\Program Files (x86)\\Steam\\userdata\\319407815\\760\\remote\\570\\screenshots")
# for file in files_and_directories:
#     x = re.search("^"+dt_string+".*.jpg$", file)
#     if x:
#         shutil.move("C:\\Program Files (x86)\\Steam\\userdata\\319407815\\760\\remote\\570\\screenshots\\"+file, "D:\\Work\\Projects\\Dota2_Guild_Image2data\\Screenshots\\"+file)

# # exec(open('D:\Work\Projects\Dota2_Guild_Image2data\Image2Text.py').read())