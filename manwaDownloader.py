from bs4 import BeautifulSoup
import requests
import time
import datetime
from datetime import datetime as dt
import os
import shutil
import pandas as pd
import numpy as np
import base64
import platform
import json
from json import loads, dumps


systemOS = platform.system()
print("Current OS: ", systemOS)
if(systemOS == 'Windows'):
    dirSeparator = '\\'
else:
    dirSeparator = '/'
dirname = os.path.dirname(__file__)

printFolder = True
lastChapter = ''
last_manga_folder_name = ''
firstPgConditionCount = 0 # counts pattern searched for starting page within list of condition
csv_location = 'D:\\WORK\\MEGA_DATA_WAREHOUSE\\CSV\\manga_sync.csv'
csv_location2 = 'D:\\WORK\\MEGA_DATA_WAREHOUSE\\CSV\\manga.csv'

# for main page data for csv 
mm_name = []
mm_banner = []
mm_host_url = []
mm_name_url = []
mm_rating = []
mm_chapters = []
mm_default = []
mm_ch_default = []

def createMangaCSV():
    nextpg = "https://manhwahentai.me/webtoon"
    i=0
    while(i<100):
        i=i+1
        tt = mainPagelistingHtml(nextpg)
        nextpg = tt
        if(nextpg == ''):
            break
    
    # Transform data into tables
    name_DF = pd.DataFrame(mm_name)
    host_DF = pd.DataFrame(mm_host_url)
    name_url_DF = pd.DataFrame(mm_name_url)
    ch_DF = pd.DataFrame(mm_chapters)
    rate_DF = pd.DataFrame(mm_rating)
    bn_DF = pd.DataFrame(mm_banner)
    offine_DF = pd.DataFrame(mm_default)
    ch_sync_DF = pd.DataFrame(mm_ch_default)
    sp_case_DF = pd.DataFrame(mm_default)
    
    MainDataFrame = pd.concat([name_DF, host_DF, name_url_DF, ch_DF, rate_DF, bn_DF, offine_DF, ch_sync_DF, sp_case_DF], axis=1)
    MainDataFrame.columns =['name', 'host_url', 'name_url', 'chapter', 'rating', 'banner', 'offline', 'chapter_sync', 'sp_case']
    print(MainDataFrame)
    MainDataFrame.to_csv(csv_location2, index=False)

    # sync with old CSV
    df = pd.read_csv(csv_location)
    # print(df) 

    print('Adding Dataframe')
    df = pd.concat([df,MainDataFrame])
    df.drop_duplicates(subset=['name_url'], keep="first", inplace=True)
    
    # print(df) 
    df.to_csv(csv_location, index=False)
    
def mainPagelistingHtml(url):
    try:
        # url_link = "https://manhwahentai.me/webtoon/"
        # url_link = "https://manhwahentai.me/webtoon/page/19/"
        url_link = url
        result = requests.get(url_link).text
        doc = BeautifulSoup(result, "html.parser")
        # generateHTMLdump(doc,2)
        # return 0
        mangas = doc.findAll('div', class_='manga')
        global mm_name, mm_banner, mm_url, mm_rating, mm_chapters
        for manga in mangas:
            m_name = manga.find('div', class_='post-title')
            m_img = manga.find('div', class_='item-thumb')
            m_img = m_img.find('img')
            try :
                m_img = m_img.attrs['src']
            except : 
                continue
            

            # save img & encoding it
            sub_dir_url2 = m_img.split('/')
            manga_chapter_imgFile = sub_dir_url2[len(sub_dir_url2)-1]
            # manga_chapter_imgFile = base64.b64encode(bytes(manga_chapter_imgFile, 'utf-8')) # bytes
            # manga_chapter_imgFile = str(manga_chapter_imgFile)
            r = requests.get(m_img, allow_redirects=True)
            open('D:\\WORK\\MEGA_DATA_WAREHOUSE\\agnam\\'+manga_chapter_imgFile, 'wb').write(r.content)
            # base64_str = b.decode('utf-8') # convert bytes to string

            # split url into host and mangaurl name
            url_temp = m_name.find('a').attrs['href']
            url_temp_arr = m_name.find('a').attrs['href'].split('/')
            name_url_temp = url_temp_arr[len(url_temp_arr)-2]
            host_url_temp = url_temp.replace('/'+name_url_temp+'/','')
            ch_temp = manga.find('a', class_='btn-link').text.replace('Chapter','').replace('Chaptre','').replace(' ','').replace('END','')
            try:
                ch_temp = float(ch_temp)
                # ch_temp = int(ch_temp)
            except ValueError:
                continue

            mm_name.append(str(m_name.find('a').text))
            mm_host_url.append(str(host_url_temp))
            mm_name_url.append(str(name_url_temp))
            # mm_url.append(str(m_name.find('a').attrs['href']))
            mm_banner.append(str(manga_chapter_imgFile))
            mm_rating.append(manga.find('div', class_='rating').text.replace('\n',''))
            mm_chapters.append(ch_temp)
            mm_default.append(0)
            mm_ch_default.append(1)

        div_nextpg = doc.find('div', class_='wp-pagenavi')
        nextpg = div_nextpg.find('a', class_='larger').attrs['href']
        print(nextpg)
        return nextpg
    except Exception as error:
        print('Error:'+repr(error))
        return ''

def mangaSync(manga_chapter_name, manga_name, mode):
    # sync and update /add
    if(mode == 0):
        df = pd.read_csv(csv_location)
        manga_chapter_name = manga_chapter_name.replace('chapter','').replace('-','')
        # print(df) 
        print('updating chapter...',manga_name, manga_chapter_name)
        df_up_index = df[(df['name_url'] == manga_name)].index
        df['chapter_sync'][df_up_index] = manga_chapter_name
        # print(df) 
        df.to_csv(csv_location, index=False)  

def declareChapterEnd(manga_chapter_name, manga_name):
    print('Last Chapter was:',manga_chapter_name)
    print('Last ',manga_chapter_name, manga_name)
    mangaSync(manga_chapter_name, manga_name, 0)

def generateHTMLdump(doc, mode=0):
    html = doc.prettify("utf-8")
    
    if(mode == 0): # full page
        html = html
    if(mode == 1): # body only
        html = doc.find('body').prettify("utf-8")
    if(mode == 2): # div
        html = doc.find('div', class_='main-col-inner').prettify("utf-8")

    with open("output1.html", "wb") as file:
        file.write(html)
    print('Error log: output1.html')
    exit()
    
def downloadpage(pageurl):
    # url_link = "https://sololeveling-manhwa.online/manga/solo-leveling-chapter-1/"
    global dirname, dirSeparator, printFolder, lastChapter, last_manga_folder_name
    
    try :
        url_link = pageurl
        result = requests.get(url_link).text
        doc = BeautifulSoup(result, "html.parser")
        
        # generateHTMLdump(doc,0)

        # column=doc.find('div', class_='column')
        column=doc.find('div', class_='entry-content')

        if(url_link.find('solo-leveling-chapter') > 0):
            nxtpg =doc.find('p', class_='gb-headline gb-headline-643cf12f gb-headline-text')
        else:
            nxtpg =doc.find('div', class_='nav-next')

        try :
            nxtpg_url = nxtpg.find('a').attrs['href']
        except : 
            nxtpg_url = ''
        
        # print(column, nxtpg,nxtpg_url)
        # exit()
        
        sub_dir_url = url_link.split('/')
        manga_folder_name = sub_dir_url[len(sub_dir_url)-3]
        manga_chapter_name = sub_dir_url[len(sub_dir_url)-2]
        # for Main Directory
        dir_manga_folder_name = os.path.join(dirname ,manga_folder_name)
        isFolderExists = os.path.exists(dir_manga_folder_name)
        if(isFolderExists == False and printFolder):
            printFolder = False
            print('Manga/Manwa:',manga_folder_name,'\n_________________________________________________')
            print('Folder:',dir_manga_folder_name)
            os.mkdir(dir_manga_folder_name)
        # exit()
        # If Manga Contain Summary content rather than chapter content then nxtpgpointer
        isProfilePage = doc.find('div', class_='profile-manga') # profile-manga, tab-summary, summary_content_wrap, c-breadcrumb-wrapper, summary-layout-1 etc.
        # print(pageurl, manga_chapter_name, last_manga_folder_name, manga_folder_name)
        if(isProfilePage != None):
            if(last_manga_folder_name == manga_chapter_name):
                print('a')
                declareChapterEnd(lastChapter, last_manga_folder_name)
                nxtpg_url = ''
                return nxtpg_url
            nxtpg_url =  pageurl[0:len(pageurl)-1]+'_1'+'/'
            return nxtpg_url
        # for Chapters
        if(manga_chapter_name == last_manga_folder_name): # manga having nxt = starting pg
            print('aa')
            declareChapterEnd(lastChapter, last_manga_folder_name)
        print('Chapter:',manga_chapter_name)
        dir_manga_chapter_name = dir_manga_folder_name + dirSeparator + manga_chapter_name
        print('Chapter Folder:',dir_manga_chapter_name)
        isChapterExists = os.path.exists(dir_manga_chapter_name)
        if(isChapterExists == True):
            shutil.rmtree(dir_manga_chapter_name)
        os.mkdir(dir_manga_chapter_name)

        # generateHTMLdump(doc,0)

        columns = column.findAll('img')
        ii = 0
        for para in columns:
            # print(para)
            
            attrs =  para.attrs
            img_url = ''
            try :
                img_url= attrs['src']
            except : 
                continue
            
            img_url= attrs['src']
            img_class= attrs['class']
            exclude1 = 'img-loading'
            if(img_class == exclude1):
                continue
            # print(img_url)
            sub_dir_url2 = img_url.split('/')
            manga_chapter_imgFile = sub_dir_url2[len(sub_dir_url2)-1]
            
            if(len(manga_chapter_imgFile) == 36):
                manga_chapter_imgFile = manga_chapter_name.replace('chapter-','').replace('-','_').replace('.jpg','')+'_'+str(ii)+'.jpg'
                ii=ii+1
            print(manga_chapter_imgFile)
            filename = os.path.join(dir_manga_chapter_name, manga_chapter_imgFile)
            
            # print(filename)
            r = requests.get(img_url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
        
        # Zip the chapter folder and deleting folder
        zip_file = shutil.make_archive(dir_manga_chapter_name, 'zip', dir_manga_chapter_name)
        if(zip_file.endswith('.zip')):
            shutil.rmtree(dir_manga_chapter_name)

        last_manga_folder_name = manga_folder_name
        lastChapter = manga_chapter_name
        if(nxtpg_url == ''):
            print('aaa')
            declareChapterEnd(lastChapter, manga_folder_name)
    except:
        generateHTMLdump(doc,0)
    return nxtpg_url
     
def download(url):
    # url = "https://sololeveling-manhwa.online/manga/solo-leveling-chapter-"
    # url = "https://manhwahentai.me/webtoon/the-17th-son/chapter-1/"
          
    # next pg or url to start
    # url = "https://manhwahentai.me/webtoon/the-17th-son/chapter-1/"
    global printFolder, lastChapter, last_manga_folder_name
    printFolder = True
    lastChapter = ''
    last_manga_folder_name = ''    
    nextpg = url
    i=0
    while(i<300):
        i=i+1
        tt = downloadpage(nextpg)
        nextpg = tt
        if(nextpg == ''):
            break
    
    sub_dir_url = url.split('/')
    manga_folder_name = sub_dir_url[len(sub_dir_url)-3]
    print('Manga Folder:', manga_folder_name)
    # exit()

    source_folder = r"D:\Work\Projects\\"+manga_folder_name+"\\"
    destination_folder = r"D:\Livings\Mobile Sync\Manga\\"+manga_folder_name+"\\"
    isDestinationFolderExists = os.path.exists(destination_folder)
    if(isDestinationFolderExists == False):
        os.mkdir(destination_folder)
    print("Moving:",source_folder, destination_folder)
    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # move only files
        if os.path.isfile(source):
            shutil.move(source, destination)
            print('Moved:', file_name)
    isSourceFolderExists = os.path.exists(source_folder)
    if(isSourceFolderExists == True):
        os.rmdir(source_folder)

def readCSVandDownloadManga():
    df = pd.read_csv(csv_location)
    # df['age'] = pd.to_numeric(df['age'], errors='coerce')
    offlined_df = df[df['offline'] == 1]
    
    chapter_to_download = offlined_df[offlined_df['chapter_sync'] < offlined_df['chapter']]
    print(chapter_to_download)

    chapter_to_download = chapter_to_download.reset_index(drop=True)
    chapter_to_download['url'] = chapter_to_download['host_url'].map(str)+'/'+chapter_to_download['name_url'].map(str)+'/chapter-'+chapter_to_download['chapter_sync'].map(str)
    # # print(chapter_to_download['url'].to_numpy())

    for url in chapter_to_download['url'].to_numpy():
        print(url+'/')
        download(url+'/')

def csvsync():
    df = pd.read_csv(csv_location)
    # df['age'] = pd.to_numeric(df['age'], errors='coerce')
    offlined_df = df[df['offline'] == 1]

    df2 = pd.read_csv(csv_location2)
    mergedStuff = pd.merge(offlined_df, df2, on=['name'], how='inner')
    mergedStuff.head()
    # df_up_index = df[(df['name_url'] == manga_name)].index
    # df['chapter_sync'][df_up_index] = manga_chapter_name
    # # print(df) 
    
    chapter_to_download = offlined_df[offlined_df['chapter_sync'] < offlined_df['chapter']]
    print(mergedStuff)

    # chapter_to_download = chapter_to_download.reset_index(drop=True)
    # chapter_to_download['url'] = chapter_to_download['host_url'].map(str)+'/'+chapter_to_download['name_url'].map(str)+'/chapter-'+chapter_to_download['chapter_sync'].map(str)
    # # # print(chapter_to_download['url'].to_numpy())

    # for url in chapter_to_download['url'].to_numpy():
    #     print(url+'/')
    #     download(url+'/')

def autoGUI(option):
    global error, pageURLchanged, firstrun
    # minimizeVSCODE()

    if(option == 1):
        # PART 1 Create Mangas CSV (1 time run in month)
        createMangaCSV()

    # PART 2 CSV Update
    if(option == 2):
        csvsync()
    
    # PART 2 Download
    if(option == 3):
        readCSVandDownloadManga()

    # both
    if(option == 4):
        autoGUI(1)
        autoGUI(2)
        autoGUI(3)
    if(option == 5):
        exit()
    exit()

def autoGUI_main():
    print('Select below option:')
    print('1: Create Mangas CSV')
    print('2: CSV Update: manga -> manga_sync ')
    print('3: Download')
    print('4: All')
    print('5: Exit')
    option = int(input("Enter your option: "))
    if(option > 0 and option <6):
        autoGUI(option)
    else:
        exit() 

autoGUI_main()
