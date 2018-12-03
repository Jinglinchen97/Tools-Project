# Tools-Project


## Description of the project:

The goal of the project is to find if there exist a relationship between stock returns and stock-related news, and to provide a method for investor to predict the return of given stock. Investor can choose a stock index as stock universe to estimate the relationship, and a stock code to predict the return according to the regression result.

**The main steps**
1. Get the stock codes of index constituents, and their most recently stock returns
2. Get the updated two days' stock-related news of index constituents from Yahoo Finance
3. Convert the quatitative news content into quantitative attitude index by sentiment analysis
4. Make OLS regression on stock returns of index constituents and information extracted from news
5. Use the parameters estimated to predict return of given stock

**About the result**

The project provide the prediction of stock return according to its recently published news.



## Group name and Section:

**Contributors (in random order):**
Nian Zhao (nz2294)
Xinyue Ruan (xr2136)
Chaoyue Zheng (cz2529)
Jinglin Chen (jc5059)

**Section:**
Sec 002


## Installation Instruction:

(1) Installtion
Library need to be installed for crawling news from Yahoo Finance:
```
!pip install requests
```
```
!pip install bs4
```
Since Yahoo Finance is a dynamic webpage, more news will be loaded through scrolling down, hence we install selenium to automate webpage
```
!pip install selenium
```
Library pandas, numpy and pandas_datareader for graping stock data:
```
!pip install pandas
```
```
!pip install pandas_datareader
```

Library nltk, vaderSentiment.vaderSentiment for sentiment analysis:
```
!pip install nltk
!pip install vaderSentiment
```
(2) Import
```
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import sent_tokenize
import pandas as pd
from pandas_datareader import data as web
import datetime
import re
import time
import numpy as np
import statsmodels.api as sm
```


## Run Instructions:


* As this is a program using the latest two days' data for prediction, latest two day's stock price need to be acquirable. You can only run the cell during stock opening day.

1. File "Tools Project Code.ipynb" in the master branch includes all codes need running; files in other branches have all been merged into this main file;
2. To start the project, you need to input the stock code (stock must be within one of the three pools: SP500,nasdaq100 and DJIA) you are interested in and select one pool the stock is from;
3. For the chromedriver in selenium, we need to download chromedriver.exe (download link: https://sites.google.com/a/chromium.org/chromedriver/home） and replace the path with your own path to chromedriver;
```
driver = webdriver.Chrome(executable_path = 'YOUR OWN PATH TO CHROMEDRIVER')
```

4. To run the program, user need to initate an object, for example:
```
a = news_stock('MMM','DJIA')
```
then user need to call several functions to get desired result:
```
a.get_stock_return()
a.get_sentiment()
a.regress()
a.prediction()
```

## Class Structure Description:
There are 4 classes in the project, functions in classes are similar to the above.  
**Classes:**  
+ Context - provide the global context of stock to predict and stock universe to estimate relationship.  
+ news - inherited from Context, includes methods related to news crawling and sentiment analysis.  
    + _scrolling_down_page(self, stock_name)
    + _get_article_link(self, results_page)
    + _get_article_content(self, all_links)
    + _artical_format(self, artical_content)
    + web_crawling(self, stock_name)
    + vader_comparison(self, artical_texts)
+ stock - inherited from Context, includes methods of getting stock universe and stock returns.  
    + _get_djia_return(self)
    + _get_sp500_codes(self)
    + _get_nasdaq100_codes(self)
    + get_stock_return(self)
+ news_stock - inherited from news and stock, includes methods of making regression and prediction.  
    + get_sentiment(self)
    + regress(self)
    + prediction(self)
 
 

## Appendix  
|File Name|Description|
|---|---|
|Tools Project Code - Class Version.ipynb|This class-version codes structure all codes into several classes, which gives a clearer clue for each step|
|Tools Project Code-Raw Version.ipynb|This raw-version file is better for learner to interpret all codes, which documents the progress we built this program step by step|
|Tools Project Code-Test Result.ipynb|As chromdriver can't execute under VM, we upload the after-running version and test result using AAPL as interested stock|


## References:
1. https://pythonprogramming.net/sp500-company-price-data-python-programming-for-finance/
