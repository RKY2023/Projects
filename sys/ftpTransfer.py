from ftplib import FTP
import os
# Audiobooks
debug_mode = False
def transferFile(ftp1, filepath, destinationfilename):
    file = open(filepath,'rb')                  # file to send
    t = ftp1.storbinary('STOR '+destinationfilename, file)     # send the file
    file.close()
    return t

def createDir(ftp1, dir):
    try:
        ftp1.mkd(dir)
    except: 
        print('--')
    if(debug_mode):
        print(ftp1.cwd(dir))

def transferFolderFiles(ftp1, rootLoc, destinationRootLocation):
    global debug_mode
    # rootLoc = 'D:\\Library\\Audiobook\\My_Audiobooks\\'
    destinationRootLocation = '/'+destinationRootLocation # '/Audiobooks'
    for path, subdirs, files in os.walk(rootLoc):
        for name in files:
            path1 = os.path.join(path, name)
            file_name = os.path.basename(path1)
            file_name_withoutextension = os.path.splitext(file_name)[0]
            file_mp3 = os.path.join(path,file_name_withoutextension+".mp3")
            file_txt = os.path.join(path,file_name_withoutextension+".txt")
            # excluding mp3 file
            if(path1==file_txt):
                continue
            if(debug_mode):
                print('Path',path1)
            foldersArray = path.replace(rootLoc,'').split('\\')
            if(debug_mode):
                print('Folder before:',ftp1.pwd())
            if(ftp1.pwd() != destinationRootLocation):
                ftp1.cwd(destinationRootLocation)
            if(debug_mode):
                print('Folder After:',ftp1.pwd())
            if(debug_mode):
                print(foldersArray)
            
            for folder in foldersArray:
                if(folder == ''):
                    continue
                print('folder created:',folder)
                createDir(ftp1, folder)
                # ftp1.cwd(folder)
                # exit()
                if(debug_mode):
                    print(ftp1.pwd())
            t = transferFile(ftp1, file_mp3, file_name_withoutextension+".mp3")
            print(file_name_withoutextension+".mp3",t)

def transferManga(ftp1, rootLoc, destinationRootLocation):
    # rootLoc = 'D:\\Library\\Audiobook\\My_Audiobooks\\'
    destinationRootLocation = '/'+destinationRootLocation # '/Audiobooks'
    for path, subdirs, files in os.walk(rootLoc):
        for name in files:
            path1 = os.path.join(path, name)
            file_name = os.path.basename(path1)
            file_name_withoutextension = os.path.splitext(file_name)[0]

            file_path = os.path.join(path,file_name)
            print('Path',path1)
            foldersArray = path.replace(rootLoc,'').split('\\')
            if(debug_mode):
                print('Folder before:',ftp1.pwd())
            if(ftp1.pwd() != destinationRootLocation):
                ftp1.cwd(destinationRootLocation)
            if(debug_mode):
                print('Folder After:',ftp1.pwd())
            if(debug_mode):
                print(foldersArray)
            
            for folder in foldersArray:
                if(folder == ''):
                    continue
                if(debug_mode):
                    print('folder created:',folder)
                createDir(ftp1, folder)
                # ftp1.cwd(folder)
                # exit()
                print(ftp1.pwd())
            t = transferFile(ftp1, file_path, file_name)
            print(file_name,t)

# transferFolderFiles('s')    
ftp1 = FTP()
# session = ftplib.FTP_TLS(host='192.168.31.26',port='2121', user='rk2023',passwd='192837465')
conn = ftp1.connect(host='192.168.31.26',port=2121)
print('Connection:', conn)
loginn = ftp1.login(user='rk2023',passwd='192837465')
print('Login:',loginn)
print('Listing DIR:',ftp1.nlst())
# print(ftp1.dir())
# print(ftp1.cwd('Audiobooks'))
# print(ftp1.cwd('/SHAREit/files/'))
print(ftp1.pwd())
# print(ftp1.mkd('Audiobooks'))
# transferFile(ftp1)                          # close file and FTP
labelBlock = '=============================='
# Modes sync(modify based on size changes), overwritefile, overwritefolder, writeonly, same

# rootLoc = 'D:\\Library\\Audiobook\\My_Audiobooks\\'
# transferFolderFiles(ftp1, rootLoc, 'Audiobooks')
# print(labelBlock, 'AudioBoook Synced', labelBlock)

# rootLoc = 'D:\Livings\Mobile Sync\Manga\\'
# transferManga(ftp1, rootLoc,'Manga')
# print(labelBlock, 'Manga Synced', labelBlock)

# rootLoc = 'D:\Music\\'
# transferManga(ftp1, rootLoc,'Music')
# print(labelBlock, 'Music Synced', labelBlock)
rootLoc = 'D:\Music\\'
transferManga(ftp1, rootLoc,'Music')
print(labelBlock, 'Music Synced', labelBlock)
ftp1.quit()

