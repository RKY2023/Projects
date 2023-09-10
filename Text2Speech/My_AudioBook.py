# Import the required module for text
# to speech conversion
import time
from gtts import gTTS
from io import BytesIO
# This module is imported so that we can
# play the converted audio
import os

def text2Speechfile(file_path,file_name, mytext):
    # https://gtts.readthedocs.io/en/latest/module.html#gtts.tts.gTTS.stream

    # Language in which you want to convert
    language = 'en'
    # Top level Domain
    toplvldom = 'co.in'

    myobj = gTTS(text=mytext, lang=language,tld=toplvldom, slow=False)

    # Saving the converted audio in a mp3 file named
    myobj.save(file_path+'\\'+file_name+".mp3")

    # # Playing the converted file
    # os.system("mpg321 welcome.mp3")

rootLoc = 'D:\\Library\\Audiobook\\My_Audiobooks\\'

for path, subdirs, files in os.walk(rootLoc):
    for name in files:
        absPath = os.path.join(path, name)
        file_name = os.path.basename(absPath)
        file_name_withoutextension = os.path.splitext(file_name)[0]
        file_mp3 = os.path.join(path,file_name_withoutextension+".mp3")
        file_txt = os.path.join(path,file_name_withoutextension+".txt")
        # excluding mp3 file
        if(absPath==file_mp3):
            continue
        print(absPath)
        # checking if mp3 created or not
        try :
            ti_c = os.path.getctime(file_mp3)
        except :
            ti_c = 0
        ti_m = os.path.getmtime(file_txt)

        if( (ti_m - ti_c) > 3600):
            file1 = os.path.join(path,file_name_withoutextension+".txt")
            fileOpened = open(file1,"r+")         
            mytext = fileOpened.read()
            print("Generating ",file_name_withoutextension+".mp3")
            text2Speechfile(path,file_name_withoutextension,mytext)

import subprocess
def scheduler(task, description, day, time, batfile):
    action = "$action = New-ScheduledTaskAction -Execute '"+batfile+"'"
    trigger = "$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek "+day+" -At "+time
    Register = "Register-ScheduledTask -Action $action -Trigger $trigger -TaskPath 'My Tasks' -TaskName '"+task+"' -Description '"+description+"'"
    cmd = action + "; " + trigger + '; ' + Register
    result = subprocess.run(['powershell', '-Command', cmd], capture_output=True, text=True)
    return result
# $action = New-ScheduledTaskAction -Execute 'D:\work\HelpDesk\Windows\windows_crons\Sunday.bat'
# $trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 12pm
# Register-ScheduledTask -Action $action -Trigger $trigger -TaskPath 'My Tasks' -TaskName 'MyAudioBook' -Description 'Sync Audiobook'
