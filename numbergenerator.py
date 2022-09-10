
from urllib import request
import requests
import time
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random

browser = webdriver.Chrome(ChromeDriverManager().install())
y=1
maxPages=2573157538607026564968244111304175730063056983979442319613448069811514699875
urladdr =  "https://privatekeys.pw/keys/bitcoin/"
indstr = "https://blockchain.info/address/"
spanstr = ['sc-1ryi78w-0', 'cILyoi', 'sc-16b9dsl-1', 'ZwupP', 'u3ufsr-0', 'eQTRKC']
boturl = "https://api.telegram.org/bot5579866377:AAEw7g1cqbXX7L_1ushBzl0gDPIjBgTIXns/sendMessage?chat_id=-656948449&text="
# Print iterations progress
calc=0
while(True):
        calc+=33
        window_before = browser.window_handles[0]
        url = urladdr+str(y)
        reqs = browser.get(url)
        time.sleep(0.5)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        items = soup.find_all('span')
        profit = items[3].text
        if profit!=' 0':
                requests.get(boturl+"Найдены деньги на странице"+str(y))
        print("Проверено адресов: "+str(calc))
        y=random.randint(0,maxPages)

                  






