from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
for i in range(1,10):
  html = urlopen('https://marianpulse.mariancollege.org/page/'+str(i))
  bs = BeautifulSoup(html, 'html.parser')
  images = bs.find_all('img', {'src':re.compile('.jpg')})
  for image in images: 
      print(image['src']+'\n')
  paragraph  = bs.find_all('p',)
  for para in paragraph:
    print(para)