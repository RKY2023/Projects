from pypdf import PdfReader, PdfWriter
import os
import json
import camelot
# python3 -m pip uninstall camelot
# python3 -m pip uninstall camelot-py
# python3 -m pip install camelot-py[cv]
import pandas as pd
import re

def notepad2data(file, debug):
    text_file = open(file, "r")
    if(debug==1):
        text_file = open("D:\Livings\special case Bank Statements.txt", "r")
    lines = text_file.readlines()
    # print(lines)
    # print(len(lines))
    dateArr=[]
    TransRefArr = []
    ChqRefArr = []
    CreditArr = []
    DebitArr = []
    BalArr = []
    # 'templine' for break in trnsaction id
    templine = ''
    for line_no,line in enumerate(lines):
        if(line_no > 72):
            # print(line)
            line = line.replace('TRANSACTION OVERVIEW','')
            if(templine == ''):
                date = line[:8]
                # print(date)
                # check first 8 char are date or not
                x = re.search("^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{2}$", date)
                if (x == None):
                    continue

            # check last char are no or not
            x = re.search("\d{1,}\.\d{2}\n", line)
            if ( x == None):
                templine = line
                continue
            else :
                line = templine + line
                # print(line,x)
                templine = ''

            # print(date, x)

            # # to check date format as PDF(DD-MM-YY)
            # dateArr.append(date)
            # to update date format as PDF(YY-MM-DD) into DBMS
            date = date[6:8]+'-'+date[3:5]+'-'+date[:2]
            dateArr.append(date)
            
            line = line[8:]
            line = line.strip()
            
            # split in texts(transaction id) and numbers(cheque no, credit, debit, balance)
            
            x = line.find('- ')
            # print(x)
            TransRefText = line[:x]
            
            match = " "+line[x:]
            # comment this for check
            match = match.split(' ')
            # print(match, len(match))
            lenchecker = len(match)
            if(len(match)!=5): # case for cheque (len=3) or other cases
                x = re.findall("(\d{1,}\.\d{2})", line) # exclude balance
                # print(line, x)
            
                # exit()
                match= []
                for i in range(5):
                    match.append('0')
                # for xi in x:
                #     for xii in xi:
                #         if(xii == ''):
                #             continue
                #         match += xii
                # match = match.replace('-','- ').replace('  ',' ')
                # match = match.split(' ')
                # print(match, len(match))
                lenchecker = len(match)
                
                # ([-]|[ ])[0-9]*([-]|[ ])*[0-9]*($|\.\d{2})
                # (\d{1,}\.\d{2})|([ ]|[-])
                x1 = re.search("([-]|[ ])[0-9]*([-]|[ ])*[0-9]*($|\.\d{2})", line)
                # print(line, x1)
                
                check_no = line[x1.start():].lstrip().split(' ')[0]
                # print(check_no)
                # exit()
                TransRefText = TransRefText[:x1.start()]
                match[1] = check_no
                match[2] = x[0] # credit
                match[4] = x[1] # balance
                if(len(x) ==2):
                    lenchecker=5
            if(lenchecker != 5):
                print('Error Line:',line,'\n len: ',lenchecker,'\n', x, x1)
                exit()
            numbers = match
            # # numbers = line[x.start():x.end()]
            # # # ChqRefArr.append(numbers)
            # # numbers = ' ' + numbers
            # # numbers = numbers.replace('  ',' ').replace('-','')
            # numbers = numbers.replace('-','')
            # numbers = numbers.split(' ')
            # print(numbers) # numbers[0] is useless as contain extra space for regex
            # if (line_no > 80):
            #     exit()
            TransRefText = TransRefText.strip()
            TransRefArr.append(TransRefText)
            ChqRefArr.append(numbers[1].replace('-',''))
            CreditArr.append(numbers[2].replace('-','0'))
            DebitArr.append(numbers[3].replace('-','0'))
            BalArr.append(numbers[4].replace('-','0'))

    # Transform data into tables
    dt_DF = pd.DataFrame(dateArr)
    tr_DF = pd.DataFrame(TransRefArr)
    ch_DF = pd.DataFrame(ChqRefArr)
    cr_DF = pd.DataFrame(CreditArr)
    db_DF = pd.DataFrame(DebitArr)
    bl_DF = pd.DataFrame(BalArr)
    MainDataFrame = pd.concat([dt_DF, tr_DF, ch_DF, cr_DF, db_DF, bl_DF], axis=1)
    MainDataFrame.columns =['Date', 'TransactionIdRef', 'ChequeRefNo', 'Credit', 'debit', 'balance']
    print(MainDataFrame)
    return MainDataFrame
    
    text_file.close()

def decryptPDF(absSourceFilePath,absDestinationFilePath,path,destinationFilename):
    # reader = PdfReader("encrypted-pdf.pdf")
    reader = PdfReader(absSourceFilePath)
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt("43652310796")
        # reader.decrypt("3107@3652")

    # Add all pages to the writer
    pages= reader.pages
    for page in pages:
        writer.add_page(page)

    # Save the new PDF to a file
    # with open("decrypted-pdf.pdf", "wb") as f:
    with open(path+"decrypted-"+destinationFilename, "wb") as f:
        writer.write(f)
    return path+"decrypted-"+destinationFilename
# decryptPDF()
def pdf2df():
    pd.reset_option("max_columns")
    # extract all the tables in the PDF file
    # abc = camelot.read_pdf("decrypted-pdf.pdf")   #address of file location
    tables = camelot.read_pdf("decrypted-"+file)   #address of file location
    # number of tables extracted
    print("Total tables extracted:", tables.n)

def usingPypdf2(absSourceFilename,file_txt):
    import PyPDF2
    pdfFileObj = open(absSourceFilename, 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    # printing number of pages in pdf file
    pages = len(pdfReader.pages)
    print('Pages', pages)
    content = ''
    for t in range(0, pages):
        print('Page::', t)
        # creating a page object
        pageObj = pdfReader.pages[t]
        
        # extracting text from page
        text = pageObj.extract_text()
        print(text)
        content = content + text
        # print(pageObj)
        # print(pageObj.images)
    
    # print(fileName)
    with open(file_txt, 'w') as f:
        f.write(content)
    # closing the pdf file object
    pdfFileObj.close()
# usingPypdf2(file)
# def croppdf(file):
# def trAy():
#     from pdfreader import SimplePDFViewer
#     fd = open(file, "rb")
#     viewer = SimplePDFViewer(fd)
#     print(viewer.render())
#     markdown = viewer.canvas.text_content
#     # print(markdown)
#     print(viewer.canvas.strings)

# trAy()
def generatefilelocation():
    rootLoc = 'D:\\Livings\\Bank Statements\\'

    for path, subdirs, files in os.walk(rootLoc):
        for name in files:
            absPath = os.path.join(path, name)
            file_name = os.path.basename(absPath)
            file_name_withoutextension = os.path.splitext(file_name)[0]
            file_pdf = os.path.join(path,file_name_withoutextension+".pdf")
            file_txt = os.path.join(path,file_name_withoutextension+".txt")
            # excluding mp3 file
            if(absPath!=file_pdf):
                continue
            print(path)
            decryptedFile = decryptPDF(file_pdf,file_txt,path,file_name_withoutextension+".pdf")
            print('Decrypted, Filename:', decryptedFile)
            usingPypdf2(decryptedFile,file_txt)
            # # checking if mp3 created or not
            # try :
            #     ti_c = os.path.getctime(file_mp3)
            # except :
            #     ti_c = 0
            # ti_m = os.path.getmtime(file_txt)

def generateTxtData():
    rootLoc = 'D:\\Livings\\Bank Statements\\'

    for path, subdirs, files in os.walk(rootLoc):
        for name in files:
            absPath = os.path.join(path, name)
            file_name = os.path.basename(absPath)
            file_name_withoutextension = os.path.splitext(file_name)[0]
            file_pdf = os.path.join(path,file_name_withoutextension+".pdf")
            file_txt = os.path.join(path,file_name_withoutextension+".txt")
            # excluding mp3 file
            if(absPath!=file_txt):
                continue
            print(file_txt)
            dataframe = notepad2data(file_txt,0)
            insertDataFrameToDatabase(dataframe)
            # # checking if mp3 created or not
            # try :
            #     ti_c = os.path.getctime(file_mp3)
            # except :
            #     ti_c = 0
            # ti_m = os.path.getmtime(file_txt)
def insertDataFrameToDatabase(dataframe):
    import pymysql as ps
    try:
        cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='sys')
        cmd=cn.cursor()
        for i,row in dataframe.iterrows():
            #here %S means string values 
            sql = "INSERT INTO sys.transactions(date, transaction_id, cheque_ref_no, credit, debit, balance) VALUES (%s,%s,%s,%s,%s,%s)"
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
    # exit()

def debugSpecialCase():
    notepad2data('', 1)
# generatefilelocation()
# dataframe = generateTxtData()

# debugSpecialCase