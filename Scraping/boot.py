import json,requests,csv
from bs4 import BeautifulSoup 


def main():
	arr=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","other"]
	fields=['Name','Address','City','Country','Booth_no',"Email","website",'url',"Contact_no","products"]
	filename="boot.csv"
	csvfile = open(filename, 'a')
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(fields) 
	for x in arr:
		r = requests.get("https://www.boot.com/vis/v1/en/directory/"+x+"?oid=58808&lang=2")
		soup = BeautifulSoup(r.content, 'html5lib')
		text =soup.find_all('div',attrs={'class':'exh-table-item'}) 
		
		for row in text:
			row_soup = BeautifulSoup(str(row))
			
			try:
				name=row_soup.find('h2',attrs={'class': "exh-table-item__name"}).text
			except Exception as e:
				print(e)
				name=''

			url = row_soup.find('h2',attrs={'class': "exh-table-item__name"}).parent['href']
			try:

				address=row_soup.find('div',attrs={'itemprop': "address"}).text
			except Exception as e:
				print(e)
				address=''
				add[0]=''
				add[1]=''
			
			if address != '':
				
				add=address.split(", ")
			
			try:
				stand=row_soup.find('div',attrs={'class': "exh-table-col exh-table-col--location"}).text
			except Exception as e:
				print(e)
				stand=''

			url="https://www.boot.com"+str(url)
			r1=requests.get(url)
			if r1== None:
				r1=''
			soup1=BeautifulSoup(r1.content,'html5lib')
			
			
			try:
				Address=soup1.find('div',attrs={'class':"push-half--bottom"}).text
				
			except Exception as e:
				print(e)
				Address=''
				ModAdd=''

			if Address != '':
				Add=Address.split(" ")
				ModAdd=''
				for i in Add:
					if((i!=' ')and(i!='\n')and(i!='\t')):
						ModAdd=ModAdd+str(i)

				#print(ModAdd)
				#exit(0)
					

			try:
				Contact=soup1.find('span',attrs={'itemprop':"telephone"}).text
			except Exception as e:
				print(e)
				Contact=''

			
			try:
				Email=soup1.find('a',attrs={'itemprop':"email"}).text
			except Exception as e:
				print(e)
				Email=''
			
			try:
				Company_url=soup1.find('a',attrs={'itemprop':"url"}).text
			except Exception as e:
				print(e)
				Company_url=''
			#print(soup1.find_all('div',attrs={'class':"div-table__cell vis-categories__content"}))
			product=''
			main_product_list =[]
			p=soup1.find("div",attrs={'id':"vis-categories-list"})
			#print(p)
			#print(type(p))
			#print("============================")
			
			#exit(0)
			try:
				product_category_parent=p.find_all("div",attrs={'class':"div-table__cell vis-categories__content"})
			
				#print(product_category_parent)
				for product_category_obj in product_category_parent:
					product_category =product_category_obj.find("p").text
					try:
						product_list_out =product_category_obj.find_all("li")
						product_list =[]
						for product_list_obj in product_list_out:
							product_list.append(product_list_obj.text)
					except Exception as e:
						product_list= None
					if product_list!=None:
						product_text=product_category+": "+str(product_list)
					else:
						product_text=product_category
					main_product_list.append(product_text)
			except Exception as e:
				print(e)
				
			# # print(type(product_category))
			# product1=[]
			# product2=''
			# product=''
			# product_head=''
			# try:
				
			# 	#print(products1)
				
			# 	#product+product categories
			# 	# product1=soup1.find('div',attrs={'class':"div-table__cell vis-categories__content"}).text
			# 	product_head = soup1.find('div',attrs={'class':"div-table__cell vis-categories__content"}).find("p").text
			# 	#print(product_head)
				
			# 	product=product+product_head+":"
			# 	#for row in soup1.find('div',attrs={'class':"div-table__cell vis-categories__content"}).find_all("li"):
			# 		#product1.append(row.text)
			# 	product1=soup1.find('div',attrs={'class':"div-table__cell vis-categories__content"}).find_all("li")
			# 	#print(product1)
			
			# 	for row in product1:
			# 		product=product+row.text+","
			# 	product=product+"\b"
			# 	#print(product)
			# 	#exit(0)
			# 	#print(product1)
			# 	#print(product1)
			# except Exception as e:
			# 	#print("product category not found")
			# 	product1=''
			# 	try:
			# 		product2=soup1.find('div',attrs={'class':"div-table__cell vis-categories__content"})
			# 		#product2=soup1.find_all('ul',attrs={'class':"ul__no-list-style-type","ng-show":"isContentActive"})
			# 		#product=product2.text
			# 		print(product2)
			# 		exit(0)
			# 		for row in product2:
			# 			print(row)
			# 		#exit(0)
					
			# 	except Exception as e:
			# 		#print("product not found")
			# 		product2=''
			# #exit(0)
			

			#print(product)
			
			#print(product)
		
			csvwriter.writerow([str(name).strip(),ModAdd,str(add[0]).strip(),str(add[1]).strip(),str(stand).strip(),str(Email).strip(),str(Company_url).strip(),url.strip(),str(Contact).strip(),main_product_list])
			
			


main()