import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
#mongo imports
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient



#<div id="nsecp" class="inprice1 nsecp" rel="42.55" data-numberanimate-value="42.55" data-numberanimate-characterheight="65" data-numberanimate-characterwidth="31" data-numberanimate-animationtimes="[10,0,10]" style="display: inline-block; vertical-align: top; height: 65px;"><div data-numberanimate-pos="2" style="width: 31px; height: 65px; overflow: hidden; display: inline-block;"><div style="backface-visibility: hidden; transform: translate3d(0px, -520px, 0px); transition: all 0ms ease-in-out 0s;">, . - + 0 1 2 3 4 5 6 7 8 9</div></div><div data-numberanimate-pos="1" style="width: 31px; height: 65px; overflow: hidden; display: inline-block;"><div style="backface-visibility: hidden; transform: translate3d(0px, -390px, 0px); transition: all 0ms ease-in-out 0s;">, . - + 0 1 2 3 4 5 6 7 8 9</div></div><div data-numberanimate-pos="0" style="width: 15px; height: 65px; overflow: hidden; display: inline-block;"><div style="backface-visibility: hidden; transform: translate3d(0px, -65px, 0px); transition: all 0ms ease-in-out 0s;">, . - + 0 1 2 3 4 5 6 7 8 9</div></div><div data-numberanimate-pos="-1" style="width: 31px; height: 65px; overflow: hidden; display: inline-block;"><div style="backface-visibility: hidden; transform: translate3d(0px, -585px, 0px); transition: all 0ms ease-in-out 0s;">, . - + 0 1 2 3 4 5 6 7 8 9</div></div><div data-numberanimate-pos="-2" style="width: 31px; height: 65px; overflow: hidden; display: inline-block;"><div style="backface-visibility: hidden; transform: translate3d(0px, -585px, 0px); transition: all 0ms ease-in-out 0s;">, . - + 0 1 2 3 4 5 6 7 8 9</div></div></div>
#/html/body/div[19]/div[2]/div[4]/div[1]/div/div[1]/div/div[1]/div[2]

def eventminer(driver):
    driver.get("https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/suzlonenergy/SE17")
    soup = BeautifulSoup(driver.page_source,features="html.parser")
        #<input id="nsespotval" type="hidden" value="43.10">
        #<div id="nsechange" class="pricupdn nsechange grn"><span class="greenuparow"></span>0.60 (1.41%)</div>
        #<p class="nseasondate">As on 29 Jan, 2024 | 09:42</p>
    change = soup.find("div",attrs={"id":"nsechange"})
    price=soup.find("input",attrs={"id":"nsespotval"})
    extract_time=soup.find("p",attrs={"class":"nseasondate"})

    return [price,change,extract_time]
"""
to write into file        
def function2(a):
    f =open("suzlon.txt","a")
    f.write(str(a))
    f.close()
"""

#driver defination
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome()


#while loop to read data continously until kill manually
i=True
while(i==True):
    try:
        currenthour = datetime.datetime.now().timetuple().tm_hour
        while(i):
            a = eventminer(driver)
            time.sleep(5)
    except(KeyboardInterrupt):
        i=False
        print("keyboard kills")
        driver.quit()
