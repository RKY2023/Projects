
# importing required modules
import PyPDF2
  
# creating a pdf file object
# pdfFileObj = open('jul.pdf', 'rb')
pdfFileObj = open('D:\Library\Civics\Constitution of India 2023050195.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
  
# printing number of pages in pdf file
pages = len(pdfReader.pages)
print('Pages', pages)

for t in range(0, 5):
    print('Page::', t)
    # creating a page object
    pageObj = pdfReader.pages[t]
    
    # extracting text from page
    print(pageObj.extract_text())
    
# closing the pdf file object
pdfFileObj.close()

# import fitz
# doc = fitz.open('108.pdf')
# for page in doc:
#   text = page.get_text()
#   print(text)