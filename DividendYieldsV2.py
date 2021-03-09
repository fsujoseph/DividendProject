# Author: Joe Caswell
# Date: 6/8/2020
# Description: This program prompts the user to create a new portfolio file containing all of their stocks, or load
# an existing one. This program simply functions as an add-on if you are curious to see the amount of dividends
# your investments are producing each year.

import os
import json
import requests
import bs4


def yn():   # Obtain yes/no response from user
    while True:
        ans = input()
        if ans.lower() == "yes":
            return True
        elif ans.lower() == "no":
            return False
        else:
            print("Please answer with yes or no.")


def login():
    """
    This function creates or loads in a user's stock portfolio as a .json file.
    """
    entries = os.listdir()                  # Lists profiles in folder
    print("Are you a returning user?")      # Checks if user is new or has profile
    check = yn()
    name = input("What is your name? ")     # Requests user's name to find profile or to create new one
    name_formatted = name.lower().replace(" ", "")+".json"   # Formats name to later be opened and edited

    if check is False and name_formatted in entries:    # Checks to make sure profile does not already exist
        print("Your portfolio already exists! Please try again.")
        print("These are the profiles that are already created: ")
        print(entries)
        access()
    elif check is False:    # Asks if user would like to make a new profile, otherwise ends program
        print("Would you like to create a new portfolio? ")
        if yn() is False:
            quit()
        else:   # Creates user profile with name formatted as .json file
            print("A new portfolio has been created called {}".format(name_formatted))
            file = open(name_formatted, 'w')     # Creates file
            dic = {}    # Empty dictionary which will contain stock name and price
            json.dump(dic, file)     # json allows dictionary to be stored in a text file (otherwise not possible)
            file.close()
            return name_formatted
    else:   # If user is returning
        if name_formatted in entries:
            print("Welcome back {}!".format(name))
            return name_formatted
        else:   # If user enters profile that does not exist asks to create new one, otherwise kill program
            print("Sorry, your portfolio is not in the files. Would you like to create a new portfolio? ")
            if yn() is True:
                file = open(name_formatted, 'w')
                dic = {}
                json.dump(dic, file)
                file.close()
                return name_formatted
            else:
                print("These are the profiles that are already created: ")
                print(entries)
                quit()


def data_entry():
    """
    This function allows the user to first view their profile. Then it contains options to add, remove, or change
    the stock holdings.
    """
    file_name = login()             # Calls login script to obtain file name
    file = open(file_name, 'r')
    portfolio = json.load(file)     # Loads file into variable
    file.close()

    print("Would you like to view your portfolio?")
    if yn():                 # Allows user to see stocks in portfolio
        for key, value in portfolio.items():
            print("{}:{}".format(key, value))
        if len(portfolio) == 0:
            print("Your portfolio is empty!")

    # Allows user to make changes to their portfolio
    print("Would you like to edit your portfolio? ")
    if yn():
        print("Would you like to add stocks? ")
        ans = yn()
        if ans is True:
            portfolio = add_stock(portfolio)
        else:
            pass
        print("Would you like to remove stocks? ")
        ans = yn()
        if ans is True:
            portfolio = remove_stock(portfolio)
        else:
            pass
        print("Would you like to change your number of shares? ")
        ans = yn()
        if ans is True:
            portfolio = change_stock(portfolio)
            return portfolio, file_name
        else:
            return portfolio, file_name
    else:
        return portfolio, file_name


def add_stock(portf):
    """
    This function contains the process for adding a stock to a profile.
    """
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
                if float(shares) > 0:
                    break
                else:
                    print("Please enter a positive number. ")
                    pass
            portf[stock] = shares


def remove_stock(portf):
    """
    This function contains the process for removing a stock to a profile.
    """
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
    """
    This function contains the process for changing the stock quantity of a profile.
    """
    while True:
        change = input("Please enter the stock you would like to change. Type done when you are finished. ")
        if change.lower() == 'done':
            return portf
        elif change.upper() not in portf:
            print("{} is not a part of your portfolio! ".format(change))
            pass
        elif change.upper() in portf:
            shares = input("How many shares of {} do you own? ".format(change.upper()))
            portf[change.upper()] = shares


def access():
    """
    This function contains the process for scraping the stock price data from Robinhood and then printing the
    dividend payout.
    """
    portfolio_and_file_name = data_entry()
    portfolio = portfolio_and_file_name[0]
    file_name = portfolio_and_file_name[1]

    dividends, value = 0, 0
    for stock, shares in portfolio.items():
        link = 'https://robinhood.com/stocks/'+stock    # Creates link to Robinhood specific to stock name
        r = requests.get(link)
        soup = bs4.BeautifulSoup(r.text, "lxml")    # Loads text data from webpage

        # The following methods work by finding out where the dividend yield is located on the webpage. Different
        # Stocks have different things available which changes the location of the dividend yield. I tested it out
        # for stocks and different ETF's so every scenario should be covered.
        price = soup.find('div', {'class': 'QzVHcLdwl2CEuEMpTUFaj'}).text
        price = price[1:]
        print('{} Price: ${}'.format(stock, price))
        div = soup.find_all('div', {'class': '_2SYphfY1DF71e5bReqgDyP'})[6].text
        div = div[14:]
        try:
            test = soup.find_all('div', {'class': '_2SYphfY1DF71e5bReqgDyP'})[10].text
        except:
            div = soup.find_all('div', {'class': '_2SYphfY1DF71e5bReqgDyP'})[2].text
            div = div[14:]
        try:
            float(div)
        except:
            div = 0
        if div == 0:
            print('{} Div: N/A'.format(stock))
        else:
            print('{} Div: {}%'.format(stock, div))
        price = price.replace(',', '')   # If the stock price is over 4 figures
        # Rung through stocks class within this for loop to get the dividends and share values
        div_value = divs_and_value(float(div), float(price), float(shares))
        dividends += div_value[0]
        value += div_value[1]

    print("Your total yearly dividends is ${:.2f}".format(dividends))
    print("Your total portfolio is worth ${:.2f}".format(value))

    # Dumps the updated portfolio back into the .json file
    file = open(file_name, 'w+')
    json.dump(portfolio, file)
    file.close()


def divs_and_value(div, price, shares):
    dividend = div * price * shares / 100
    value = shares * price
    return dividend, value


if __name__ == "__main__":
    access()