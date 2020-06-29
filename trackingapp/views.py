from django.shortcuts import render
# Create your views here.
from .models import User,Login
from django.http import HttpResponse,HttpResponseRedirect
import pandas as pd
import matplotlib.pyplot as  plt
import requests 
from bs4 import BeautifulSoup 
import csv 
from datetime import date
import os.path
from requests import ConnectionError
from django.views.generic import View 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.http import JsonResponse
import json
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def index(request):
    return render(request,"home.html")
def home(request):
    return render(request,"home.html")    
    
def register(request):
    if request.method=='POST':
        name    =  request.POST.get('name')
        email =  request.POST.get('email')
        uname   =  request.POST.get('uname')
        pwd     =  request.POST.get('pwd')
        if Login.objects.filter(username=uname).exists():
            return render(request, "register.html", {'error_msg':'Username already taken'})
        else:   
            loginobj=Login()
            loginobj.username=uname
            loginobj.password=pwd
            loginobj.rollid=2
            loginobj.save()

            registerobj=User()
            registerobj.loginid=loginobj
            registerobj.name=name
            registerobj.email=email
            registerobj.save()
           
       


        
        
    return render(request,"register.html")    

def login(request):
     if request.method=='POST':
         unam=request.POST.get('uname')
         passw=request.POST.get('pass')
            
         if Login.objects.filter(username=unam,password=passw).exists():
             user=Login.objects.get(username=unam)
             if user.rollid==1:
                 return HttpResponse("admin")
             elif user.rollid==2:
                 request.session['user_id'] = user.id
                 userobj = User.objects.get(loginid=user)
                 return render(request,'ph.html', {'userinfo': userobj})   
         
         return render(request, "login.html", {'error_msg':'username or password  is incorrect'})
     return render(request,'login.html')

def v(request):
    return render(request,'v.html') 

def ph(request):
    return render(request,'ph.html') 

def logout(request):
    del request.session['user_id']
    return render(request,'home.html')    

def visual(request):
    #with open('abcd.csv', 'r') as file:
        #reader = csv.reader(file)
    d=pd.read_csv('abcde.csv')
    print(d.head())   
    #d.plot(kind='line',color='blue')
    plt.bar(d['date'],d['price'])
    plt.xlabel('date')
    plt.ylabel('price') 
    #plt.show()    
    plt.savefig('food2.png')
    return render(request, 'ph.html')


def alert(request):
    if request.method=='POST':
        url=request.POST.get('url')
        r = requests.get(url) 

        soup = BeautifulSoup(r.content, 'html5lib') 
        pri = soup.find('div', attrs={'class':'_1vC4OE _3qQ9m1'})
        nam1 = soup.find('span', attrs={'class':'_35KyD6'})
       

        Date=date.today()
        print(Date)
        x=nam1.get_text()
        if os.path.isfile("{}.csv".format(x)):
            with open("{}.csv".format(x), 'a', newline="") as f:
                fieldnames = ['date', 'Price']
                thewriter = csv.DictWriter(f, fieldnames = fieldnames)
                thewriter.writerow({'date': Date, 'Price': pri.get_text().replace("₹","").replace(",","")})
             
                    
        else:   
            with open("{}.csv".format(x), 'w', newline="") as f:
                fieldnames = ['date', 'Price']
                thewriter = csv.DictWriter(f, fieldnames = fieldnames)
                thewriter.writeheader() 
                #update on next execution?:???
                thewriter.writerow({'date': Date, 'Price': pri.get_text().replace("₹","").replace(",","")})
            
        from shutil import copyfile
        copyfile("{}.csv".format(x),"static/v/javascripts/abcde.csv")

        x=nam1.get_text()
        d=pd.read_csv("{}.csv".format(x))
        #plt.bar(d['date'],d['Price'])
        plt.plot(d['date'],d['Price'])
        plt.xlabel('date')
        plt.ylabel('price') 
        plt.savefig("{}.png".format(x))   
        plt.savefig("static/latest.png")     
           



        return render(request, 'v.html')

    return render(request, 'alert.html')

currentprice=[1]

def Scrap(request):
    if request.method=='POST':
        try:
            url=request.POST.get('url')
            urlcopy=str(url)
            amazon=urlcopy.find("amazon")
            flipkart=urlcopy.find("flipkart")
            reliance=urlcopy.find("reliance")
            dec=urlcopy.find("decathlon")
            marian=urlcopy.find("marian")
            if(reliance!=-1):
                print("ya reliance")
                r = requests.get(url) ##############key operation !!!!!!!!!!!
                
                soup = BeautifulSoup(r.content, 'html5lib')
                pri = soup.find('span', attrs={'class':'pdp__offerPrice'})
                nam1 = soup.find('div', attrs={'class':'pdp__title'})
                if(pri!=None):
                    name=nam1.get_text()
                    price=int(pri.get_text().replace("₹","").replace(",","").replace(" ",""))
                    currentprice[0]=price
                    context={'price':currentprice[0],'name':name} 
                    return render(request, 'chart.html',context=context)
                return render(request, 'ph.html')


            elif (amazon!=-1):
                print("ya amazon")
                hdr5 = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding': 'none',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Connection': 'keep-alive'}
                r = requests.get(url,headers=hdr5) ##############key operation !!!!!!!!!!!

                soup = BeautifulSoup(r.content, 'html5lib')       
                pri = soup.find('span', attrs={'class':'a-size-medium a-color-price priceBlockBuyingPriceString'})
                nam1 = soup.find('span', attrs={'class':'a-size-large'})
                if(pri!=None):
                    print(nam1)
                    image=soup.find('div',attrs={'class':"a-dynamic-image  a-stretch-horizontal"})
                    print(image)
                    price=pri.get_text().replace("₹","").replace(",","").replace(" ","").replace(u'\xa0', '')
                    print(price)
                    currentprice[0]=int(float(price))
                    context={'price':currentprice[0],'name':nam1.get_text} 
                    return render(request, 'chart.html',context=context)
                return render(request, 'ph.html',)       
            elif flipkart != -1:
                print("ya flipkatrt")
                r = requests.get(url) ##############key operation !!!!!!!!!!!
                print(str(r).find("404"))
                if (str(r).find("404"))==-1:
                    print("yes")
                    soup = BeautifulSoup(r.content, 'html5lib') 
                    pri = soup.find('div', attrs={'class':'_1vC4OE _3qQ9m1'})
                    if(pri!=None):
                        #print(pri)
                        #image=soup.find('div',attrs={'class':"_3BTv9X _3iN4zu"})
                        #print(image)
                        nam1 = soup.find('span', attrs={'class':'_35KyD6'})
                        name=nam1.get_text()
                        price=pri.get_text().replace("₹","").replace(",","") 
                        currentprice[0]=int(price)
                        context={'price':currentprice[0],'name':name}
                        return render(request, 'chart.html',context=context)
                    return render(request,'ph.html')
                return render(request,'ph.html') 
            
  
                
            elif(marian!=-1):
                print("marian")
                img=[]
                parag=[]
                for i in range(1,7):
                    html = urlopen('https://marianpulse.mariancollege.org/page/'+str(i))
                    bs = BeautifulSoup(html, 'html.parser')
                    images = bs.find_all('img', {'src':re.compile('.jpg')})
                    paragraph  -= bs.find_all('p',)          
                    for image in images: 
                        img.append(image['src'])
                    for para in paragraph:
                        parag.append(para.get_text())               
                return render(request, 'marian.html',{ 'paragraph':parag,
                            'images':img }) 


            elif dec != -1:
                print("ya decathlon")
                #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                r = requests.get(url) ##############key operation !!!!!!!!!!!
                soup = BeautifulSoup(r.content, 'html5lib') 
                pri = soup.find('span', attrs={'class':'price_tag text-center d-inline-block'})
                nam=soup.find('span', attrs={'class':'_35KyD6'})
                print(pri)
                return render(request, 'ph.html')
            else:
                print("not a flip")
                return render(request, 'ph.html')
        except(ConnectionError):
            print ("Exception is :")
            return render(request, 'ph.html')

        #validate = URLValidator()

    return render(request, 'ph.html')





from django.views.generic import View 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.http import JsonResponse
import json
import random
class Chart(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'chart.html') 

class ChartData(APIView): 
    authentication_classes = [] 
    permission_classes = []  
    def get(self, request, format = None): 
        labels = [ 
           '',
            '',
             '',
              '',
               '',
                '',
                 '',
                  '',
                   '',
                    '',
                     '',
                      '',
                       '',
                        '',
            ] 
        chartLabel = "price"
        chartdata=[0,0,0,0,0,0,0,0,0,0]
        for i in range(10):
           x=random.randint(currentprice[0]-int(currentprice[0]/6), currentprice[0]+int(currentprice[0]/6))
           chartdata[i]=x
        
        chartdata=chartdata+currentprice
        print(chartdata)
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data) 
