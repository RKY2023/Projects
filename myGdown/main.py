# # https://drive.google.com/drive/folders/1S05GF1v6tNnPJ__DeMtFYntItTylCDUV
# import gdown

# # file_url = 'https://drive.google.com/uc?id=0B9P1L--7Wd2vNm9zMTJWOGxobkU'
# folder_url = 'https://drive.google.com/drive/folders/1S05GF1v6tNnPJ__DeMtFYntItTylCDUV'



# file_output = '20150428_collected_images.tgz'
# # folder_output = '20150428_collected_images.zip'
# # gdown.download(url, output, quiet=False)
# # gdown.download_folder(folder_url, quiet=True)
# gdown.download_folder(folder_url, quiet=True, use_cookies=False)
import os
import datetime
from download_folder import download_folder
import json 



def PrashantTiwariPDF():
    with open(r'D:\Work\MEGA_DATA_WAREHOUSE\JSON\PT current affair pdf link.json') as f:
        json_data = json.load(f)
        
    yr = datetime.date.today().strftime("%y")
    mn = datetime.date.today().strftime("%b")
    dt = datetime.date.today().strftime("%d")
    day = datetime.date.today().strftime('%A')
    dir_name = dt+' '+mn+' '+yr
    if (day=='Sunday'):
        print('Its Sunday, No pdf today')
        return
    # print(dir_name)
    
    isExistYear = os.path.exists('D:\\Learnings\\UPSC\\Prashant Tiwari - Hindu News Paper\\'+yr)
    isExistMonth = os.path.exists('D:\\Learnings\\UPSC\\Prashant Tiwari - Hindu News Paper\\'+yr+'\\'+mn)
    if (isExistYear==False):                                                  
        os.mkdir('D:\\Learnings\\UPSC\\Prashant Tiwari - Hindu News Paper\\'+yr)
    if (isExistMonth==False):
        os.mkdir('D:\\Learnings\\UPSC\\Prashant Tiwari - Hindu News Paper\\'+yr+'\\'+mn)
    tt = os.mkdir('D:\\Learnings\\UPSC\\Prashant Tiwari - Hindu News Paper\\'+yr+'\\'+mn+'\\'+dir_name)
    source = 'Current Affairs'
    destination = 'D:\\Learnings\\UPSC\\Prashant Tiwari - Hindu News Paper\\'+yr+'\\'+mn+'\\'+dir_name

    # Download per day pdf from prashant tiwari PDF Google drive link   
    # folder_url = 'https://drive.google.com/drive/folders/12ZjlQ7LDiHkq2sVMZRszrBy3lXWmBUBZ'
    folder_url = json_data['d_link']
    
    dff = download_folder(folder_url, quiet=True, use_cookies=False)
    # gather all files
    af = allfiles = os.listdir(source)
    
    # iterate on all files to move them to destination folder
    for f in allfiles:
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination, f)
        mav = os.rename(src_path, dst_path)
    os.rmdir(source)
    print(tt,'t',dff,'-',af,'|-',mav,'|-|')
    
    MsgOut = ''
    for f in af:
        MsgOut = MsgOut+ f+'\n'
    return MsgOut

msg = PrashantTiwariPDF()
from winotify import Notification, audio
toast = Notification(app_id="Newspaper PDF", title="Prashant Tiwari PDF Downloaded",msg=msg,duration="long",icon=r"D:\Icons\pdf2.ico")
toast.set_audio(audio.Default, loop=False)
toast.show()

