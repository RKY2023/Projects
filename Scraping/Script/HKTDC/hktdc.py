import json,requests,csv,sys
from bs4 import BeautifulSoup
import urllib

def main():
	fields=['name','country','companyAddress','telephone','website','boothNumber','productCategory']
	filename="International toy & game fair 1.csv"
	csvfile = open(filename,'w')
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields)
	# count=1
	for i in range(1,5):


		with urllib.request.urlopen("https://api-fair.hktdc.com/fair-company/v1/companies?language=en&fairSymbol=hktoyfair&pageItem=60&page="+str(i)) as url:
			# print("https://api-fair.hktdc.com/fair-company/v1/companies?language=en&fairSymbol=hkwatchfair&pageItem=60&page="+str(i))
			# continue;
			data = json.loads(url.read().decode())
			data1=data['hits']
		for hits in data1:
			print(hits['hits'][0]['name'])
			print(hits['hits'][0]['country'])
			print(hits['hits'][0]['companyAddress'])
			print(hits['hits'][0]['telephone'])
			print(hits['hits'][0]['website'])
			# strwebsite=website.rsplit(" ",2)[0] 
			print(hits['hits'][0]['boothNumber'])
			print(hits['hits'][0]['productCategory'])
			csvwriter.writerow([hits['hits'][0]['name'],hits['hits'][0]['country'],hits['hits'][0]['companyAddress'],hits['hits'][0]['telephone'],hits['hits'][0]['website'],hits['hits'][0]['boothNumber'],hits['hits'][0]['productCategory']])	
main()