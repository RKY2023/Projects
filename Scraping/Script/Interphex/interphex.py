import json,requests,csv,sys
from bs4 import BeautifulSoup 


def main():
	# arr=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","other"]
	fields=['Name','Address','City','Country','Booth_no','Email','website','url','Contact_no','products']
	filename="prateek.csv"
	csvfile = open(filename, 'w')
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields)
	count = 1	
	final_data =[]
	for i in range(9):
		url = 'https://www.interphex.com/en/Show-Info/Exhibitor-List/?lo=0&rpp=552&startRecord='+str(count)
		count+=64
		# http_proxy  = "http://36.67.93.220:3128"
		# https_proxy = "https://183.89.138.200:8080"
		# ftp_proxy   = "ftp://36.67.93.220:3128"

		# proxyDict = { 
		# 				"http"  : http_proxy, 
		# 				"https" : https_proxy, 
		# 				"ftp"   : ftp_proxy
		# 			}

		r = requests.get(url)
		print("Url: "+str(url))
		soup = BeautifulSoup(r.content, 'html5lib')
		ul =soup.find('ul',attrs={'id':'searchResultsList'}) 
		li = ul.find_all("li")
		last_page = soup.select('ul > li:nth-of-type(7) > a')[0]['href']
		for data in li:
			scrapped_data ={}
			name=data.find('h3',attrs={'class':"name"})
			if name!= None:
				print("Selected Name: "+str(name.text))
				scrapped_data['name'] = name.text
				scrapped_data['url'] ="https://www.interphex.com"+(data.find('h3',attrs={'class':"name"}).find("a", recursive=False)['href'])
				r= requests.get(scrapped_data['url'])	
				child_soup = BeautifulSoup(r.content,"html5lib")
				address = child_soup.find("div",attrs={"class":"addresses tabContent"})
				if address != None:
					address = address.find("dd",attrs={"class":"contact"})
					scrapped_data['country'] =address.find("span",attrs={"class":"country-name"}).text.strip()
					scrapped_data['city'] =address.find('span',attrs={'class':'locality'})
					if scrapped_data['city'] !=None:
						scrapped_data['city'] =address.find('span',attrs={'class':'locality'}).text.strip()
					else:
						scrapped_data['city']=""		
					scrapped_data['address']=address.find("div",attrs={"class":"adr"}).text.strip()
					scrapped_data['address']=scrapped_data['address'].replace("\n","")
					scrapped_data['address'] = ' '.join(scrapped_data['address'].split())
				else:
					scrapped_data['country'] =""
					scrapped_data['city'] =""
					scrapped_data['address']=""
				stand=child_soup.find("div",attrs={"class":"standDetails"})
				scrapped_data['stand']=stand.find("li",attrs={"class":"exhibitor"})
				if scrapped_data['stand'] !=None:
					scrapped_data['stand']=stand.find("li",attrs={"class":"exhibitor"}).text.strip()
				else:
					scrapped_data['stand']=""
				contact_no=child_soup.find("div",attrs={"class":"tel"})
				if contact_no != None:
					scrapped_data['contact_no']=contact_no.find("span",attrs={"class":"value"})
					if scrapped_data["contact_no"] != None:
						scrapped_data["contact_no"] = scrapped_data["contact_no"].text.strip()
					else:
						scrapped_data["contact_no"] = ""
				else:
					scrapped_data["contact_no"] = ""
				products=child_soup.find("div",attrs={"class":"inner-attribute-container inner-attribute-container-0 tabContent"})
				if products != None:
					products=products.find_all("dd")
					products_list =[]
					for prod in products :
						products_list.append(prod.contents[0].strip())
					scrapped_data["products"]=products_list
				else:
					scrapped_data["products"]=""
				print(scrapped_data)
				final_data.append(scrapped_data)
				csvwriter.writerow([scrapped_data["name"],scrapped_data["address"],scrapped_data["city"],scrapped_data["country"],scrapped_data["stand"],"","",scrapped_data["url"],scrapped_data["contact_no"],scrapped_data["products"]])		
			
	
		
main()