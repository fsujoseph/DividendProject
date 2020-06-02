# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:37:55 2020

@author: fsujo
"""

import bs4
import requests


# Main function to compute total dividend yield
def main():
    MSFTprice = float(PriceMSFT())
    MSFTdiv = float(DivMSFT())
    DKNGprice = float(PriceDKNG())
    DKNGdiv = float(DivDKNG())
    RTXprice = float(PriceRTX())
    RTXdiv = float(DivRTX())
    PEPprice = float(PricePEP())
    PEPdiv = float(DivPEP())
    KOprice = float(PriceKO())
    KOdiv = float(DivKO())
    QQQprice = float(PriceQQQ())
    QQQdiv = float(DivQQQ())
    LMTprice = float(PriceLMT())
    LMTdiv = float(DivLMT())
    Tprice = float(PriceT())
    Tdiv = float(DivT())
    DISprice = float(PriceDIS())
    DISdiv = float(DivDIS())
    Oprice = float(PriceO())
    Odiv = float(DivO())
    
    inv = msft*MSFTprice+dkng*DKNGprice+rtx*RTXprice+pep*PEPprice+ko*KOprice+qqq*QQQprice+lmt*LMTprice+t*Tprice+dis*DISprice+o*Oprice
    totalinv = inv+cash
    print('Your total investments are worth {:.2f}$'.format(totalinv))
    
    totaldiv = (msft*MSFTdiv*MSFTprice+dkng*DKNGprice*DKNGdiv+rtx*RTXprice*RTXdiv+pep*PEPprice*PEPdiv+ko*KOprice*KOdiv+qqq*QQQprice*QQQdiv+lmt*LMTprice*LMTdiv+t*Tprice*Tdiv+dis*DISprice*DISdiv+o*Oprice*Odiv)/100
    print('Your total yearly dividend yield is {:.2f}$'.format(totaldiv))
    
    weightdiv = (msft*MSFTdiv*MSFTprice+dkng*DKNGprice*DKNGdiv+rtx*RTXprice*RTXdiv+pep*PEPprice*PEPdiv+ko*KOprice*KOdiv+qqq*QQQprice*QQQdiv+lmt*LMTprice*LMTdiv+t*Tprice*Tdiv+dis*DISprice*DISdiv+o*Oprice*Odiv)/(inv)
    print('Your total weighted dividend yield is {:.2f}%'.format(weightdiv))

# Shares owned
msft = 5
dkng = 22
rtx = 6
pep = 1
ko = 2
qqq = 2
lmt = 1
t = 7
dis = 4
o = 1
cash = 12.89

# Scrape stock price
def PriceMSFT():
    r = requests.get('https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('MSFT Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivMSFT():
    r = requests.get('https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('MSFT Div: N/A\n')
    else:
        print('MSFT Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PriceDKNG():
    r = requests.get('https://finance.yahoo.com/quote/DKNG?p=DKNG&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('DKNG Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivDKNG():
    r = requests.get('https://finance.yahoo.com/quote/DKNG?p=DKNG&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('DKNG Div: N/A\n')
    else:
        print('DKNG Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PriceRTX():
    r = requests.get('https://finance.yahoo.com/quote/RTX?p=RTX&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('RTX Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivRTX():
    r = requests.get('https://finance.yahoo.com/quote/RTX?p=RTX&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('RTX Div: N/A\n')
    else:
        print('RTX Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PricePEP():
    r = requests.get('https://finance.yahoo.com/quote/PEP?p=PEP&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('PEP Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivPEP():
    r = requests.get('https://finance.yahoo.com/quote/PEP?p=PEP&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('PEP Div: N/A\n')
    else:
        print('PEP Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PriceKO():
    r = requests.get('https://finance.yahoo.com/quote/KO?p=KO&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('KO Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivKO():
    r = requests.get('https://finance.yahoo.com/quote/KO?p=KO&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('KO Div: N/A\n')
    else:
        print('KO Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PriceQQQ():
    r = requests.get('https://finance.yahoo.com/quote/QQQ?p=QQQ&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('QQQ Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivQQQ():
    r = requests.get('https://robinhood.com/stocks/qqq')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('div',{'class':'_1o4PJLud46X1hGKRyPgyLI'})[2].text
    div = div[0:4]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('QQQ Div: N/A\n')
    else:
        print('QQQ Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PriceLMT():
    r = requests.get('https://finance.yahoo.com/quote/LMT?p=LMT&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('LMT Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivLMT():
    r = requests.get('https://finance.yahoo.com/quote/LMT?p=LMT&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('LMT Div: N/A\n')
    else:
        print('LMT Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PriceT():
    r = requests.get('https://finance.yahoo.com/quote/T?p=T&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('T Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivT():
    r = requests.get('https://finance.yahoo.com/quote/T?p=T&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('T Div: N/A\n')
    else:
        print('T Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PriceDIS():
    r = requests.get('https://finance.yahoo.com/quote/DIS?p=DIS&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('DIS Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivDIS():
    r = requests.get('https://finance.yahoo.com/quote/DIS?p=DIS&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('DIS Div: N/A\n')
    else:
        print('DIS Div: {}%\n'.format(div))
    return div

# Scrape stock price
def PriceO():
    r = requests.get('https://finance.yahoo.com/quote/O?p=O&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print('O Price: {}$'.format(price))
    return price
      
# Scrape dividend percentage
def DivO():
    r = requests.get('https://finance.yahoo.com/quote/O?p=O&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    div = soup.find_all('tr',{'class':'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'})[12].text
    div = div[30:34]
    try:
        float(div)
    except: 
        div = 0
    if div == 0:
        print('O Div: N/A\n')
    else:
        print('O Div: {}%\n'.format(div))
    return div
main()