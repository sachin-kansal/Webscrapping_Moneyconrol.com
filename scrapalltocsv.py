from webscrapping import Moneycontrol

def fun1():
    print("Welcome to Webscrapping Moneycontrol website")
    print("Home page url -->", Moneycontrol.url)
    #Moneycontrol.companylist()
    for i in Moneycontrol.extractingurl().keys():
        Moneycontrol.get_scrapped_data(i)
fun1()
