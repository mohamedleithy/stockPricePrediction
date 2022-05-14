from datetime import date
from pstats import Stats
import string
from traceback import print_tb
from unicodedata import name
from attr import attr, attrs
from bs4 import BeautifulSoup
from certifi import contents
from matplotlib.pyplot import text
from more_itertools import unique_everseen
import requests, re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from sympy import true
from selenium.webdriver.common.keys import Keys
from sympy import content
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd




amznStocks =[] 
applStock =[] 


def cleanTweet(t): 

    t = re.sub(r'http\S+', '', t)
    t = " ".join(filter(lambda x:x[0]!='#', t.split()))
    t = " ".join(filter(lambda x:x[0]!='$', t.split()))
    


    return t



def getAaplTweets():

    url = 'https://twitter.com/search?q=%24AAPL&src=typeahead_click&f=top'
    
    # browser = webdriver.Chrome(executable_path='/Users/leithy/Downloads/chromedriver')

    # browser.get(url)
    # time.sleep(30)

      
    # elem = browser.find_element_by_tag_name("html")

    # no_of_pagedowns = 10000

    # f = open("aaplTweets.html", "w")

    # while no_of_pagedowns:
    #     elem.send_keys(Keys.PAGE_DOWN)
    #     time.sleep(0.5)
    #     if(no_of_pagedowns%15==0):
    #         content = browser.page_source
    #         f.write(content)
    #     no_of_pagedowns-=1
    #     print(no_of_pagedowns)

    # f.close()
    
    with open('aaplTweets.html', 'r') as f:

         contents = f.read()
    
    soup = BeautifulSoup(contents, 'html5lib')
    tweets = soup.find_all('div', attrs={'class':'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'})
    ts = soup.find_all('time')
    print(len(tweets))
    print(len(ts))
    
    
    for i in range(len(tweets)):
        print(tweets[i].get_text())
        print(ts[i]['datetime'].partition('T')[0])
        tweet_dict = {
        'tweet' : cleanTweet(tweets[i].get_text().rstrip()),
        'date' : ts[i]['datetime'].partition('T')[0], 
        }
        applStock.append(tweet_dict)

    df = pd.DataFrame(applStock)
    df.to_csv('applTweets.csv')

def uniqueCSV():
    with open('applTweets.csv', 'r') as f, open('unique.csv', 'w') as out_file:
        out_file.writelines(unique_everseen(f))

    file_name = "applTweets.csv"
    file_name_output = "unique.csv"

    df = pd.read_csv(file_name, sep="\t or ,")
    df.drop_duplicates(subset=None, inplace=True)
    df.to_csv(file_name_output, index=False)


def main(): 

    getAaplTweets()

    uniqueCSV()
    



main()