#!/usr/bin/env python3

#import the library
import requests
from bs4 import BeautifulSoup

all_links = []
url = "https://finance.yahoo.com/quote/"+ str(stock_name) +"/?p=" + str(stock_name)
#send the request and get the response
response = requests.get(url)
