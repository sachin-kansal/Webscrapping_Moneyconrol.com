from webscrapping import Moneycontrol

def main():
    print("Welcome to Webscrapping Moneycontrol website")
    print("Home page url -->", Moneycontrol.url)
    #Moneycontrol.companylist()
    c_name=input("\nPlease enter the name of stock from above list:")

    i=True
    while i is True:
        if c_name not in Moneycontrol.extractingurl().keys():
            print("please check the value belongs to the list and is correct")
            c_name=input("\nPlease enter the name of stock from above list:")
        else:
            Moneycontrol.get_scrapped_data(c_name)
            print("\n to Quit enter Exit as Value")
            c_name=input("\nPlease enter the name of stock from above list:")
            
        if c_name=="Exit" or c_name=="exit" or c_name=="EXIT":
            i=False
if __name__=="__main__":
    Moneycontrol.companylist()
    main()
