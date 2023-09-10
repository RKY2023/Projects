from bs4 import BeautifulSoup
import requests
import csv
import time
import re

""" Website Scrapper For mapyourshow.com events"""
""" Written by Deepali Aggarwal """
""" for any support write me on : deepalin71@gmail.com """

# list of urls to be parsed
eventNames = ["amerimold20","bio2020","nafa20","atd2020"]

headers = {'x-requested-with': 'XMLHttpRequest'}

def getData(url):
	r = requests.get(url, headers=headers)
	return r.json()['DATA']['results']['exhibitor']['hit']

def writecsv(fileName = '', eleType='row', dataList = {}):
	mod = 'w' if eleType == 'header' else 'a'
	csv_columns = ['name','address','city','country','phone','website','booth_no','src_url','products']
	try:
		with open('/home/times/Desktop/mapyourshow_8_0/'+fileName+'mys_8_0_Scrap.csv', mod) as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
			if eleType == 'row':
				writer.writerow(dataList)
	except Exception as e:
		print('Unable to write file :',e)
	finally:
		csvfile.close()

def main():
	for eName in eventNames:
		writecsv(eName, 'header')
		writecsv(eName, 'row', {'name' : 'name','address' : 'address','city' : 'city','country' : 'country','phone' : 'phone','website' : 'website','booth_no' : 'booth_no','src_url' : 'src_url','products' : 'products'})


		exhData = getData('https://'+eName+'.mapyourshow.com/8_0/ajax/remote-proxy.cfm?action=search&search=*&searchtype=exhibitoralpha&searchsize=9540&start=0&show=exhibitor&lazyload=true&size-exhibitor=9540')
		
		for i in exhData:
			val = {'name' : '','address' : '','city' : '','country' : '','phone' : '','website' : '','booth_no' : '','src_url' : '','products' : ''}

			val['name'] = str(i['fields']['exhname_t']).strip()
			val['src_url'] = 'https://'+eName+'.mapyourshow.com/8_0/exhibitor/exhibitor-details.cfm?exhid='+str(i['fields']['exhid_l']).strip()

			if "booths_la" in i['fields']:
				val['booth_no'] = ','.join(str(x) for x in i['fields']['booths_la'])

			try:
				childhtm = requests.get(val['src_url']).text
				sp2 = BeautifulSoup(childhtm, 'html.parser')
			except Exception as e:
				print("page not found",e)
				
			if sp2:
				if sp2.find('span', {'class': 'muted'}, string = 'Address:'):
					try: 
						val['address'] = str(sp2.find('span', {'class': 'muted'}, string = 'Address:').next_sibling).strip()
						if sp2.find('span', {'class': 'muted'}, string = 'Address2:'):
							val['address'] = val['address'] + ", " + str(sp2.find('span', {'class': 'muted'}, string = 'Address:').next_sibling).strip()
					except:
						print(val['src_url'], '[address]', e)

				if sp2.find('span', {'class': 'muted'}, string = 'City:'):
					try: 
						val['city'] = str(sp2.find('span', {'class': 'muted'}, string = 'City:').next_sibling).strip()
					except:
						print(val['src_url'], '[city]', e)

				if sp2.find('span', {'class': 'pr2'}, string = 'Country:'):
					try:
						val['country'] = sp2.find('span', {'class': 'pr2'}, string = 'Country:').find_parent('p').find_all('span', {'class': 'lh-list'})[1].get_text().strip("\n\t\r")
					except Exception as e:
						print(val['src_url'], '[country]', e)


				if(sp2.find('span', {'class': 'pr2'}, string = 'Phone:')):
					try:
						val['phone'] = sp2.find('span', {'class': 'pr2'}, string = 'Phone:').find_parent('p').find_all('span', {'class': 'lh-list'})[1].get_text().strip("\n\t\r")
					except Exception as e:
						print(val['src_url'], '[phone]', e)
					
				if sp2.find('span', {"class": "muted"}, string= re.compile("Website:")):
					try:
						val['website'] = sp2.find('span', {"class": "muted"}, string= re.compile("Website:")).find_parent('p', {'class': 'lh-copy'}).find('a').get('href')
					except Exception as e:
						print(val['src_url'], '[website]', e)

				try:
					if sp2.find('h2', {"class": "js-ResultHeader"}, string= re.compile("Product Categories")):
						val['products'] = "|".join([prod.get_text().strip('\n\t') for prod in sp2.find('h2', {"class": "js-ResultHeader"}, string= re.compile("Product Categories")).find_parent('section', {'class': 'mb0-last'}).find_all('li', {"class": "o-List_Columns_Item"})])
				except Exception as e:
					print(val['src_url'], 'products', e)

			writecsv(eName, 'row', val)
		print("%s [Done]" % eName)

if __name__ == '__main__':
	main()