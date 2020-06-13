
import os
import json
import requests
import bs4

# Obtain  response from user
def yn():
    while True:
        ans = input()
        if ans.lower() == "yes":
            return True
        elif ans.lower() == "no":
            return False
        else:
            print("Please answer with yes or no.")

# Guides user to login with previously saved profile or create new one
def login():
    # Lists profiles in folder
    entries = os.listdir()
    # Checks if user is new or has profile
    print("Are you a returning user?")
    check = yn()
    # Requests users name to find profile or to create new one
    name = input("What is your name? ")
    # Formats name to later create it in proper format
    name_form = name.lower().replace(" ","")+".json"

    # Checks to make sure profile does not already exist
    if check is False and name_form in entries:
        print("Your portfolio already exists! Please try again.")
        quit()
    # Asks if user would like to make a new profile, otherwise ends program
    elif check is False:
        print("Would you like to create a new portfolio? ")
        ans = yn()
        if ans is False:
            quit()
        # Creates user profile with name formatted as .json file and initializes and empty dictionary
        else:
            print("A new portfolio has been created called {}".format(name_form))
            file = open(name_form,'w')
            dic = {}
            json.dump(dic,file)
            file.close()
            return name_form
    # If user is returning
    else:
        if name_form in entries:
            print("Welcome back {}!".format(name))
            return name_form
        # If user enters profile that does not exist asks to create new one, otherwise kill program and show files
        else:
            print("Sorry, your portfolio is not in the files. Would you like to create a new portfolio? ")
            ans = yn()
            if ans is True:
                file = open(name_form, 'w')
                dic = {}
                json.dump(dic, file)
                file.close()
                return name_form
            else:
                print("These are the profiles that are already created: ")
                print(entries)
                quit()

def data_entry():
    # Calls login script to obtain file name
    file_name = login()

    # Loads file into variable
    file = open(file_name, 'r')
    portf = json.load(file)
    file.close()

    # Allows user to see stocks in portfolio
    print("Would you like to view your portfolio?")
    ans = yn()
    if ans is True:
        for key in portf:
            print("{}:{}".format(key, portf[key]))
        if len(portf) == 0:
            print("Your portfolio is empty!")
    else:
        pass

    # Allows user to make changes to their portfolio
    print("Would you like to edit your portfolio? ")
    ans = yn()
    if ans is True:
        print("Would you like to add stocks? ")
        ans = yn()
        if ans is True:
            portf = add_stock(portf)
        else:
            pass
        print("Would you like to remove stocks? ")
        ans = yn()
        if ans is True:
            portf = remove_stock(portf)
        else:
            pass
        print("Would you like to change your number of shares? ")
        ans = yn()
        if ans is True:
            portf = change_stock(portf)
            return portf, file_name
        else:
            return portf, file_name
    else:
        return portf, file_name

def add_stock(portf):
    # Allows user to add stocks and quantities to portfolio
    while True:
        stock = (input("What is the name of the stock (shortened version)? Type done when you are finished. ")).upper()
        if stock.lower() == "done":
            return portf
        elif stock.lower() in portf:
            print("You already own {}!".format(stock))
            pass
        else:
            while True:
                shares = input("How many shares of {} do you own? ".format(stock))
                try:
                    shares = int(shares)
                    break
                except ValueError:
                    print("Please enter an integer. ")
                    pass
        portf[stock] = shares

def remove_stock(portf):
    # Allows user to remove stocks
    while True:
        remove = input("Please enter the stock you would like to remove. Type done when you are finished. ")
        if remove.lower() == 'done':
            return portf
        elif remove.upper() in portf:
            del portf[remove.upper()]
        else:
            print("{} is not a part of your portfolio! ".format(remove))
            pass

def change_stock(portf):
    # Allows user to adjust stock shares
    while True:
        change = input("Please enter the stock you would like to change. Type done when you are finished. ")
        if change.lower() == 'done':
            return portf
        elif change.upper() not in portf:
            print("{} is not a part of your portfolio! ".format(change))
            pass
        elif change.upper() in portf:
            while True:
                shares = input("How many shares of {} do you own? ".format(change))
                try:
                    shares = int(shares)
                    break
                except ValueError:
                    print("Please enter an integer. ")
                    pass
            portf[change.upper()] = shares

# Access stocks
def access():
    portfname = data_entry()
    portf = portfname[0]
    file_name = portfname[1]

    dividends = 0
    value = 0
    for stock, shares in portf.items():
        link = 'https://robinhood.com/stocks/'+stock
        r = requests.get(link)
        soup = bs4.BeautifulSoup(r.text, "lxml")

        price = soup.find('div',{'class':'QzVHcLdwl2CEuEMpTUFaj'}).text
        price = price[1:]
        print('{} Price: ${}'.format(stock,price))


        div = soup.find_all('div', {'class': '_2SYphfY1DF71e5bReqgDyP'})[2].text
        div = div[14:]
        try:
            float(div)
        except:
            div = soup.find_all('div', {'class': '_2SYphfY1DF71e5bReqgDyP'})[6].text
            div = div[14:]
        try:
            float(div)
        except:
            div = 0
        # if div == 0:
        #     print('{} Div: N/A'.format(stock))
        # else:
        #     print('{} Div: {}%'.format(stock,div))

        info = Stocks(stock, shares, price, div)
        dividends += info.dividends()
        value += info.value()

    print("Your total yearly dividends is ${:.2f}".format(dividends))
    print("Your total portfolio is worth ${:.2f}".format(value))

    file = open(file_name, 'w+')
    json.dump(portf, file)
    file.close()

class Stocks:
    def __init__(self,stock,shares,price,div):
        self.stock = stock
        self.shares = float(shares)
        self.price = float(price)
        self.div= float(div)

    def dividends(self):
        dividend = self.div*self.price*self.shares/100
        return dividend

    def value(self):
        value = self.shares*self.price
        return value



access()