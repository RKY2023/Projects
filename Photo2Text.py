import easyocr
reader = easyocr.Reader(['en'])
results = reader.readtext(r'C:\Users\XRAJ2\Downloads\Screenshot_2022-06-18-15-11-59-227_co.gradeup.android.jpg')
#a.jpg = D:\Work\a.jpg
text=''
for result in results:
	text += result[1] + ' '
with open("Image2Text.txt", "w") as scones:
	contents = "".join(text)
	scones.write(contents)