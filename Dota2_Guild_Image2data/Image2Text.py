# # print("Welcome to Python")
# from os import closerange
# from tkinter.tix import IMAGE
# from PIL import Image
# # pip install Pillow
# import pytesseract as tess
# # pip install pytesseract
# # pip install tesseract
# # pip install tesseract-ocr
# tess.pytesseract.tessetact_cmd = r'C:\Users\XRAJ2\AppData\Local\Programs\Python\Python310\Scripts\pytesseract.exe'
# # tess.pytesseract.tessetact_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# # tessdata_dir_config = '--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"'
# # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# # It's important to include double quotes around the dir path.


 
# # image = r'D:\488242.jpg'
# image = r'D:\Work\Projects\Dota2_Guild_Image2data\tt.png'
# text = tess.image_to_string(Image.open(image), lang="eng")
# # text = tess.image_to_string(Image.open(image), lang='eng', config=tessdata_dir_config)
# # text = tess.image_to_string(Image.open('D:\Work\Projects\Dota2_Guild_Image2data.etst.png'))
# # text = tess.image_to_string(Image.open('D:\\488242.jpg'))

# print(text) 
###############################
import os
import cv2
# pip uninstall opencv-python-headless -y 
# pip install opencv-python --upgrade
import numpy as np
import re
import pandas
from datetime import datetime
from datetime import timedelta
import easyocr

import  pymysql as ps

path = 'D:\\Work\\Projects\\Dota2_Guild_Image2data\\Screenshots\\'
text = ''
now = datetime.now()
dt_string = now.strftime("%Y%m%d")
files_and_directories = os.listdir(path)
# for file in files_and_directories:
#   x = re.search("^"+dt_string+".*.jpg$", file)
#   if x:
#     print(path+file)
# exit()
for file in files_and_directories:
  x = re.search("^"+dt_string+".*.jpg$", file)
  if x:
    img = cv2.imread(path+file)
    # rows, cols, _ = img.shape
    # print("Rows", rows)
    # print("Cols", cols)

    # crop image
    crop_image = img[370:910, 277:908 ]
    if files_and_directories.index(file) == 4:
      crop_image = img[820:910, 277:908 ]
    # imgRes = cv2.imshow("Cut image", crop_image)
    # cv2.imshow("image", img)
    # cv2.waitKey(0)

    cv2.imwrite(path+file, crop_image)
    # cv2.imwrite('sc1_crop1.png', img[370:415, 277:908])
    # cv2.imwrite('sc1_crop2.png', img[415:460, 277:908])
    # cv2.imwrite('sc1_crop3.png', img[460:505, 277:908])
    # cv2.imwrite('sc1_crop4.png', img[505:550, 277:908])
    # cv2.imwrite('sc1_crop5.png', img[550:595, 277:908])
    # cv2.imwrite('sc1_crop6.png', img[595:640, 277:908])
    # cv2.imwrite('sc1_crop7.png', img[640:685, 277:908])
    # cv2.imwrite('sc1_crop8.png', img[685:730, 277:908])
    # cv2.imwrite('sc1_crop9.png', img[730:775, 277:908])
    # cv2.imwrite('sc1_crop10.png', img[775:820, 277:908])
    # cv2.imwrite('sc1_crop11.png', img[820:865, 277:908])
    # cv2.imwrite('sc1_crop12.png', img[865:910, 277:908])
    # totalTT =""
    # for i in range (1,12):
    #   reader = easyocr.Reader(['en'], gpu=True)
    #   results = reader.readtext("sc1_crop"+str(i)+".png")
    #   text = ''
    #   for result in results:
    #       text += result[1] + ' '
    #   print(text)
    #   totalTT += text
    #   os.remove("sc1_crop"+str(i)+".png")

    # Convert image to text
    reader = easyocr.Reader(['en'])

    results = reader.readtext(path+file)
    #a.jpg = D:\Work\a.jpg

    for result in results:
        text += result[1] + ' '

# text = text.replace(' Yester ',' Yesterday ')
text = re.sub(r'(Yester)\w+', 'Yesterday', text)
print(text)
# os.remove("sc1_crop.png")

#####################

# f = open("D:\Work\Projects\demo.txt", "r")
# # print(f.read())
# for x in f:
#   print(x)
#   print('\n\n')

text = text.strip()
# text = "Collapse collapsein c: BHANGI LORD 217,460 GP Today Main|IEnu Kaze SENIOR BHANGI 102,410 GP Monday D@T{2:) SENIOR BHANG| 90,780 Friday TacticalDot SENIOR BHANGI 80,310 GP Today Rosu SENIOR BHANGI 65,020 GP 23/4/2022 TckngMad SENIOR BHANGI 64,470 GP Today Irv07cs083 SENIOR BHANGI "
# #x = re.search("/(Today|Yesterday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)/g", txt)
# matches = re.findall('(Today|Yesterday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)', txt, re.DOTALL)
# print(matches)
rgxDate = re.compile("(Today|Yesterday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|((0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}))")
rgxRole = re.compile("(BHANGI LORD|SENIOR BHANGI|MIDDLE BHANGI|JUNIOR BHANGI|LEAD BHANGI|KICK LIST)")
# for m in p.finditer(text):
#     print(m.start(), m.group())
Arr =[]
lastpos = 0
for m in rgxDate.finditer(text):
  Arr.append(text[lastpos: m.start()+len(m.group())])
  lastpos = m.start()+len(m.group())
print(Arr)
name = []
role = []
gp = []
date = []
for ln in Arr:
  lastpos1 = 0
  for m in rgxRole.finditer(ln):
    name.append(ln[lastpos1: m.start()].lstrip())
    role.append(m.group())
    lastpos1 = m.start()+len(m.group())
    templn = ln[lastpos1 : len(ln)]
    for n in rgxDate.finditer(templn):
      date.append(n.group())
      gp.append(templn[0:n.start()].replace(',', '').replace('+', '').replace('GP', '').strip())
print(name)
print(role)
print(gp)
print(date)

mydataset = {
  'name': name,
  'roles': role,
  'gp': gp,
  'date': date
}

myvar = pandas.DataFrame(mydataset)
myvar = myvar.drop_duplicates()
print(myvar)

newFile = []
prevLine = ''

path = 'D:\\Work\\Projects\\Dota2_Guild_Image2data\\Screenshots\\'
text = ''
now = datetime.now()
today = datetime.today()
# print(datetime.today().strftime('%Y%m%d'))
# exit()

dt_today = now.strftime("%d/%m/%Y")
dt_yesterday = (today - timedelta(days = 1)).strftime("%d/%m/%Y")
arrDay2Date = []
beginDate = (today - timedelta(days = 2)).strftime("%d/%m/%Y")
# print(beginDate)
for i in range (2,9):
    dt_temp = (today - timedelta(days = i)).strftime("%d/%m/%Y")
    dt_day = (today - timedelta(days = i)).strftime("%A")
    arrDay2Date.append([dt_day,dt_temp])

myvar.loc[myvar["name"] == "", "name"] = 'NONE'
myvar.loc[myvar["date"] == "Today", "date"] = dt_today
myvar.loc[myvar["date"] == "Yesterday", "date"] = dt_yesterday
for i in range (0,7):
    myvar.loc[myvar["date"] == arrDay2Date[i][0], "date"] = arrDay2Date[i][1]

expiries = []
temp_dt1 = myvar['date']
for row in temp_dt1:
    expire = datetime.strptime(row, '%d/%m/%Y').strftime('%Y/%m/%d')
    expiries.append(expire)
# print(len(expiries))
# print(len(myvar))
myvar["date"] = expiries
# print(expiries)
print(myvar.to_string()) 
# myvar.to_csv(path+'Dota2 Guild '+now.strftime("%Y%m%d")+'_tt.csv', index = None)

# storing this dataframe in a csv file
myvar.to_csv(path+'Dota2 Guild '+now.strftime("%Y%m%d")+'.csv', index = None)

try:
    cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='dota2')
    cmd=cn.cursor()
    for i,row in myvar.iterrows():
        #here %S means string values 
        sql = "INSERT INTO dota2.guild_scrapped(name, role, gp, active_date) VALUES (%s,%s,%s,%s)"
        cmd.execute(sql, tuple(row))
        print("Record inserted")
        # the connection is not auto committed by default, so we must commit to save our changes
        cn.commit()
    # query="select * from guild_scrapped"
    
    # cmd.execute(query)
    
    # rows=cmd.fetchall()
    
    # # print(rows)
    # for row in rows:
    #     for col in row:
    #         print(col,end=' ')
    #     print()
    
    cn.close()

except Exception as e:
    print(e)