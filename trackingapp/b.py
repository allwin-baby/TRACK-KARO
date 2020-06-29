

#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "https://www.flipkart.com/iqoo-3-quantum-silver-128-gb/p/itm7d075bc17be11?pid=MOBFP4P2NBTJYC5J&lid=LSTMOBFP4P2NBTJYC5JXXTSRK&marketplace=FLIPKART&srno=b_1_1&otracker=hp_bannerads_1_1.bannerAdCard.BANNERADS_2DFOE0GNVFM4&fm=organic&iid=2afd15c2-e58b-48bc-a197-1bf2ea2915f4.MOBFP4P2NBTJYC5J.SEARCH&ppt=browse&ppn=browse&ssid=zkj4vjqh280000001583262410582"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 

price = []
name =[] # a list to store quotes 
price = []
quote ={}
pri = soup.find('div', attrs={'class':'_1vC4OE _3qQ9m1'})
nam1 = soup.find('div', attrs={'class':'_9-sL7L'})
pri1=str(pri)
print(nam1)

with open('scrap9.csv', 'w', newline="") as f:
	fieldnames = ['Product Name', 'Price']
	thewriter = csv.DictWriter(f, fieldnames=fieldnames)

	thewriter.writeheader()
	

	thewriter.writerow({'Product Name': nam1.get_text(), 'Price': pri.get_text().replace("₹","").replace(",","")})
    
# for i in range(len(name)): 
# 	result[i].append(name[i])
# print(result[0])
	# quote = {} 
	# quote['theme'] = row.h5.text 
	# quote['url'] = row.a['href'] 
	# quote['img'] = row.img['src'] 
	# quote['lines'] = row.h6.text 
	# quote['author'] = row.p.text 
	# quotes.append(quote) 

# filename = 'inspirational_quotes.csv'
# with open(filename, 'wb') as f: 
# 	w = csv.DictWriter(f,['theme','url','img','lines','author']) 
# 	w.writeheader() 
# 	for quote in quotes: 
# 		w.writerow(quote)