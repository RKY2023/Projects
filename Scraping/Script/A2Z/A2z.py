import json,requests,csv
from bs4 import BeautifulSoup 


def main():
	arr=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","other"]
	fields=['Name','Booth_no','Address','City','Country',"website","Contact_no",'product','url']
	filename="tpe20.csv"
	csvfile = open(filename, 'w')
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields) 
	final_data=[]

	url='https://s23.a2zinc.net/clients/tmg/tpe20/Public/exhibitors.aspx?Index=All'
	r = requests.get(url)
	print("Url: "+str(url))
	soup = BeautifulSoup(r.content, 'html5lib')
	table=soup.find('table',attrs={'class':'table table-striped table-hover'})
	tr=table.find_all('tr')
	for data in tr:
		scrapped_data ={}
		name=data.find('td',attrs={'class':'companyName'})
		if name !=None: 
			scrapped_data['name']=name.text
			scrapped_data['url']='https://s23.a2zinc.net/clients/tmg/tpe20/Public/'+(data.find('td',attrs={'class':'companyName'}).find("a", recursive=False)['href'])
			Booth_no=data.find('td',attrs={'class':'boothLabel'})
			if Booth_no!=None:
				scrapped_data['Booth_no']=Booth_no.find('a').text
			else:
				scrapped_data['Booth_no']=""
			r= requests.get(scrapped_data['url'])	 		
			child_soup =BeautifulSoup(r.content,"html5lib")
			Address=child_soup.find('div',attrs={'class':'BoothContactInfo'})
			if Address!=None:
				scrapped_data['Address']=Address.find('span',attrs={'class':'BoothContactAdd1'})
				if scrapped_data['Address']!=None:
					scrapped_data['Address']=scrapped_data['Address'].text.strip()
				else:
					scrapped_data['Address']=""	
				scrapped_data['city']=Address.find('span',attrs={'class':'BoothContactCity'})
				if scrapped_data['city']!=None:
					scrapped_data['city']=scrapped_data['city'].text.strip()
				else:
					scrapped_data['city']=""	
				scrapped_data['Country']=Address.find('span',attrs={'class':'BoothContactCountry'})
				if scrapped_data['Country']!=None:
					scrapped_data['Country']=scrapped_data['Country'].text.strip()
				else:
					scrapped_data['Country']=""	
				scrapped_data['website']=Address.find('span',attrs={'class':'BoothContactUrl'})
				if scrapped_data['website']!=None:
					scrapped_data['website']=scrapped_data['website'].find('a').text.strip()
				else:
					scrapped_data['website']=""	
				scrapped_data['Contact_no']=Address.find('span',attrs={'class':'BoothContactPhone'})
				if scrapped_data['Contact_no']!=None:
				 	scrapped_data['Contact_no']=scrapped_data['Contact_no'].text.strip()
				else:
				 	scrapped_data['Contact_no']=""	
			else:
				scrapped_data['Address']=""
				scrapped_data['city']=""
				scrapped_data['Country']=""
				scrapped_data['website']=""
				scrapped_data['Contact_no']=""
			product=child_soup.find('div',attrs={'class':'ProductCategoryContainer'})
			if product!=None:
				scrapped_data['product']=product.find_all('li',attrs={'class':'ProductCategoryLi'})
				if scrapped_data['product']!=None:
					scrapped_data['product']=scrapped_data['product']
					scrapped_data['product']=product.text.strip()
					scrapped_data['product']=scrapped_data['product'].replace("\n","")
					scrapped_data['product'] = ' '.join(scrapped_data['product'].split())
					# scrapped_data['product']=scrapped_data['product'].split(" , ")	
				else:
					scrapped_data['product']=""
			else:
				scrapped_data['product']=""		
			print(scrapped_data)
			final_data.append(scrapped_data)
			csvwriter.writerow([scrapped_data['name'],scrapped_data['Booth_no'],scrapped_data['Address'],scrapped_data['city'],scrapped_data['Country'],scrapped_data['website'],scrapped_data['Contact_no'],scrapped_data['product'],scrapped_data['url']])
main()			
