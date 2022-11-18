import requests
from bs4 import BeautifulSoup

url = "https://www.moneycontrol.com/india/stockpricequote/"


def ScrappingQuote_moneycontrol(c_url): #to get all the quotes given Specific url 
    r=requests.get(c_url)
    #print(type(r))
    ls=[]
    dic={}
    if r.status_code==200: #checking for access
        soup=BeautifulSoup(r.text,features="html.parser") #soup created
        table_list_raw=soup.find_all("tbody") #splitting element at <tbody>
        for j in range(2,6):    #looping inended data
            table1=table_list_raw[j].text.split("\n")
            for i in table1:
                if (i.isspace()) or i=="" or i=='i':   #garbage cleaning
                    continue
                else:
                    ls.append(i.strip()) #data collected
        #managing data in dicionary
        i=0
        exceptions=["Beta","TTM EPS See historical trend","TTM PE See historical trend","P/B See historical trend"]
        while i<len(ls)-1:
            if ls[i] in exceptions:
                dic[ls[i]]=[ls[i+1],ls[i+2]]
                i=i+4-1
            else:
                dic[ls[i]]=ls[i+1]
                i=i+2
        return dic
    else: #if web page not present
        return "Status code error {}".format(r.status_code)
        
def extractingurl(url="https://www.moneycontrol.com/india/stockpricequote/"): # by default take url data for all web
    dic={}
    r=requests.get(url)
    if r.status_code==200:
        soup=BeautifulSoup(r.text,features="html.parser")
        tdls=soup.find_all("td")
        for i in range(1,len(tdls)):
            if tdls[i].text.strip("\n")=='':
                break
            elif i%3!=0:
                url = str(tdls[i]).split('"')[3]
                name = tdls[i].text.strip("\n")
                dic[name]=url
            else:
                url = str(tdls[i]).split('"')[5]
                name = tdls[i].text.strip("\n")
                dic[name]=url
        return dic
    
def get_scrapped_data(name): #get data based on name from dic and url="https://www.moneycontrol.com/india/stockpricequote/"
    url_data=extractingurl()
    data=ScrappingQuote_moneycontrol(url_data[name])
    for j,k in data.items():
        print(j,"-->",k)

def companylist():
    for i in extractingurl().keys(): print("{0}".format(i),end="--")


    















    
