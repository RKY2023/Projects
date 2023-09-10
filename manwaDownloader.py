from bs4 import BeautifulSoup
import requests
import time
import datetime
from datetime import datetime as dt
import os
import shutil
import pandas as pd
import base64

import platform
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
def makecbz():
    exit()
def declareChapterEnd(manga_chapter_name):
    print('Last Chapter was:',manga_chapter_name)
# for main page data for csv 
mm_name = []
mm_banner = []
mm_url = []
mm_rating = []
mm_chapters = []

def mainPagelistingHtml__pager():
    nextpg = "https://manhwahentai.me/webtoon"
    i=0
    while(i<40):
        i=i+1
        tt = mainPagelistingHtml(nextpg)
        nextpg = tt
        if(nextpg == ''):
            break
    
    # Transform data into tables
    dt_DF = pd.DataFrame(mm_name)
    tr_DF = pd.DataFrame(mm_chapters)
    ch_DF = pd.DataFrame(mm_url)
    cr_DF = pd.DataFrame(mm_rating)
    bn_DF = pd.DataFrame(mm_banner)
    MainDataFrame = pd.concat([dt_DF, tr_DF, ch_DF, cr_DF, bn_DF], axis=1)
    MainDataFrame.columns =['name', 'chapter', 'url', 'rating', 'banner']
    print(MainDataFrame)
    MainDataFrame.to_csv('D:\\WORK\\MEGA_DATA_WAREHOUSE\\CSV\\manga.csv')

def mainPagelistingHtml(url):
    try:
        # url_link = "https://manhwahentai.me/webtoon/"
        # url_link = "https://manhwahentai.me/webtoon/page/19/"
        url_link = url
        result = requests.get(url_link).text
        doc = BeautifulSoup(result, "html.parser")
        # html = doc.prettify("utf-8")
        html = doc.find('div', class_='main-col-inner').prettify("utf-8")
        with open("output1.html", "wb") as file:
            file.write(html)
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
            mm_name.append(m_name.find('a').text)
            mm_url.append(m_name.find('a').attrs['href'])
            mm_banner.append(manga_chapter_imgFile)
            mm_rating.append(manga.find('div', class_='rating').text.replace('\n',''))
            mm_chapters.append(manga.find('a', class_='btn-link').text)
        div_nextpg = doc.find('div', class_='wp-pagenavi')
        nextpg = div_nextpg.find('a', class_='larger').attrs['href']
        print(nextpg)
        return nextpg
    except Exception as error:
        print('Error:'+repr(error))
        return ''

def downloadpage(pageurl):
    # url_link = "https://sololeveling-manhwa.online/manga/solo-leveling-chapter-1/"
    global dirname, dirSeparator, printFolder, lastChapter, last_manga_folder_name

    try :
        url_link = pageurl
        result = requests.get(url_link).text
        doc = BeautifulSoup(result, "html.parser")
        
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
                declareChapterEnd(manga_chapter_name)
                nxtpg_url = ''
                return nxtpg_url
            nxtpg_url =  pageurl[0:len(pageurl)-1]+'_1'+'/'
            return nxtpg_url
        # for Chapters
        if(manga_chapter_name == last_manga_folder_name): # manga having nxt = starting pg
            declareChapterEnd(lastChapter)
        print('Chapter:',manga_chapter_name)
        dir_manga_chapter_name = dir_manga_folder_name + dirSeparator + manga_chapter_name
        print('Chapter Folder:',dir_manga_chapter_name)
        isChapterExists = os.path.exists(dir_manga_chapter_name)
        if(isChapterExists == True):
            shutil.rmtree(dir_manga_chapter_name)
        os.mkdir(dir_manga_chapter_name)

        # # print(doc)
        # html = doc.prettify("utf-8")
        # with open("output1.html", "wb") as file:
        #     file.write(html)
        # exit()
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
            declareChapterEnd(manga_chapter_name)
    except:
        html = doc.find('body').prettify("utf-8")
        with open("output1.html", "wb") as file:
            file.write(html)
        print('Error log: output1.html')
        exit()
    return nxtpg_url
     
def download():
    # url = "https://sololeveling-manhwa.online/manga/solo-leveling-chapter-"
    
    # for i in range(1,201):
    #     url_link = url+str(i)+'/'
    #     print(url_link)
    #     tt = downloadpage(url_link)
    
    # next pg or url to start
    url = "https://manhwahentai.me/webtoon/sex-stop-watch/chapter-18/"
    # https://mangahentai.me/manga-hentai/excuse-me-this-is-my-room-mgh-0016/chapter-1/
    # https://mangahentai.me/manga-hentai/ones-in-laws-virgins-mgh-0016/chapter-1/
    # https://manhwahentai.me/webtoon/what-do-you-take-me-for-webtoon-manhwa-hentai-manhwa0017/chapter-1/
    # https://manhwahentai.me/webtoon/the-perfect-roommates-webtoon-manhwa-hentai-manhwa0017/chapter-1/
    # https://manhwahentai.me/webtoon/young-boss-webtoon-manhwa-hentai-manhwa0017/chapter-1/
    # https://manhwahentai.me/webtoon/weak-point-webtoon-manhwa-hentai-manhwa0017/chapter-1/
    # https://manhwahentai.me/webtoon/love-square-manhwa0017/chapter-1/
    # https://manhwahentai.me/webtoon/dance-departments-female-sunbaes-manhwa-hentai-001/
    # https://manhwahentai.me/webtoon/lets-hang-out-from-today/
    # https://manhwahentai.me/webtoon/park-moojik-hit-the-jackpot/
    # https://manhwahentai.me/webtoon/wanna-live-by-the-countryside/
    # https://manhwahentai.me/webtoon/sex-stop-watch/
    nextpg = url
    i=0
    while(i<200):
        i=i+1
        tt = downloadpage(nextpg)
        nextpg = tt
        if(nextpg == ''):
            break
    
    sub_dir_url = url.split('/')
    manga_folder_name = sub_dir_url[len(sub_dir_url)-3]
    

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
download()
# mainPagelistingHtml__pager()
