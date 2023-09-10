import os
import time
import pyautogui
import os
import re
import shutil
from datetime import datetime
time.sleep(30)
pyautogui.click()
pyautogui.click()
pyautogui.moveTo(360, 1024, 1)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(770, 125, 1)
pyautogui.click()
time.sleep(1)
# select list in GP decending order
pyautogui.moveTo(720, 362, 1)
pyautogui.click()
time.sleep(1)
pyautogui.click()
time.sleep(1)
# scroll list //45px per item
pyautogui.moveTo(915, 375, 1)
time.sleep(1)
pyautogui.press('f12')
time.sleep(1)
pyautogui.dragTo(915, 507, 2, button='left')
time.sleep(2)
pyautogui.press('f12')
time.sleep(1)
pyautogui.dragTo(915, 640, 2, button='left')
time.sleep(2)
pyautogui.press('f12')
time.sleep(1)
pyautogui.dragTo(915, 773, 2, button='left')
time.sleep(2)
pyautogui.press('f12')
time.sleep(1)
pyautogui.dragTo(915, 915, 2, button='left')
time.sleep(2)
pyautogui.press('f12')
time.sleep(1)
pyautogui.moveTo(1895, 30, 1)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(855, 580, 1)
pyautogui.click()
time.sleep(1)

# Move Screenshot to Work dir
now = datetime.now()
dt_string = now.strftime("%Y%m%d%H")
files_and_directories = os.listdir("C:\\Program Files (x86)\\Steam\\userdata\\319407815\\760\\remote\\570\\screenshots")
for file in files_and_directories:
    x = re.search("^"+dt_string+".*.jpg$", file)
    if x:
        shutil.move("C:\\Program Files (x86)\\Steam\\userdata\\319407815\\760\\remote\\570\\screenshots\\"+file, "D:\\Work\\Projects\\Dota2_Guild_Image2data\\Screenshots\\"+file)

# exec(open('D:\Work\Projects\Dota2_Guild_Image2data\Image2Text.py').read())