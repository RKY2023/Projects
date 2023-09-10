## Drive File download start ##
import gdown
# folderurl = "https://drive.google.com/drive/folders/18ZUNHNUG5WoTdAWGbha12gjcndqp2JRW"
folderurl = "https://drive.google.com/drive/folders/1S05GF1v6tNnPJ__DeMtFYntItTylCDUV"

output = 'file.zip'
outputfolder = 'file.txt'
# url = "https://drive.google.com/file/d/1qy10dGIK35t-yB3HlgYCNwrLjyLDkJ50"
# url = url.replace('drive.google.com/file/d/','drive.google.com/uc?id=')

# prefix = "https://drive.google.com/uc?/export=download&id="

# gdown.download(url, output, quiet=False) #download file
id = "1S05GF1v6tNnPJ__DeMtFYntItTylCDUV"
id = "18ZUNHNUG5WoTdAWGbha12gjcndqp2JRW"

gdown.download_folder(id=id, quiet=True, use_cookies=False) # download folder
## Drive File download end ##