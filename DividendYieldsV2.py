
import os
import json

def yn():
    while True:
        ans = input()
        if ans.lower() == "yes":
            return True
        elif ans.lower() == "no":
            return False
        else:
            print("Please answer with yes or no.")


def login():
    entries = os.listdir()
    print("Are you a returning user?")
    check = yn()
    name = input("What is your name? ")
    name_form = name.lower().replace(" ","")+".json"
    if check is False and name_form in entries:
        print("Your portfolio already exists! Please try again.")
        quit()
    elif check is False:
        print("Would you like to create a new portfolio? ")
        ans = yn()
        if ans is False:
            quit()
        else:
            print("A new portfolio has been created called {}".format(name_form))
            file = open(name_form,'w')
            dic = {}
            json.dump(dic,file)
            file.close()
            return name_form
    else:
        if name_form in entries:
            print("Welcome back {}!".format(name))
            return name_form
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
                quit()

def data_entry():
    file_name = login()

    file = open(file_name, 'r')
    portf = json.load(file)
    file.close()

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
        else:
            return portf
    else:
        return portf

def add_stock(portf):
    while True:
        stock = input("What is the name of the stock (shortened version)? Type done when you are finished. ")
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
    while True:
        remove = input("Please enter the stock you would like to remove. Type done when you are finished. ")
        if remove.lower() == 'done':
            return portf
        elif remove in portf:
            del portf[remove]
        else:
            print("{} is not a part of your portfolio! ".format(remove))
            pass

def change_stock(portf):
    while True:
        change = input("Please enter the stock you would like to change. Type done when you are finished. ")
        if change.lower() == 'done':
            return portf
        elif change not in portf:
            print("{} is not a part of your portfolio! ".format(change))
            pass
        elif change in portf:
            while True:
                shares = input("How many shares of {} do you own? ".format(change))
                try:
                    shares = int(shares)
                    break
                except ValueError:
                    print("Please enter an integer. ")
                    pass
            portf[change] = shares

def data_prep():
    portf = data_entry()
    print(portf)
    print(portf[0])

class Stocks:
    def __init__(self,stock,shares,price,dividend):
        self.stock() = stock


data_prep()