# Tools-Project
### Description of the project:
The goal of the project is to

**The main steps**
1. Input stockcode(within S&P500) you want
2. Get the updated two days' stock-related news from Yahoo Finance
3. Get corresponding two days' stock return 
4. 
5.

**About the result**


### Group name and Section:
**Contributors (in random order):**
Nian Zhao (nz2294)
Xinyue Ruan (xr2136)
Chaoyue Zheng (cz2529)
Jinglin Chen (jc5059)

**Section:**
Sec 002


### Installation Instruction:
(1) Installtion
Library need to be installed for crawling news from Yahoo Finance:
```
!pip install requests

```
```
!pip install bs4

```
Since Yahoo Finance is a dymanic webpage, more news will be loaded through scrolling down, hence we install selenium to automate webpage
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
!pip install pandas_datareader

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



### Run Instructions:
Run instruction:

** As this is a program using the latest two days' data for prediction, latest two day's stock price need to be acquirable. You can only run the cell during stock opening day.

1. File "Tools Project Code.ipynb" in the master branch includes all codes need running; files in other branches have all beened merged into this main file;
2. To start the project, you need to input the stock code (stock must be within one of the three pools: SP500,nasdaq100 and DJIA) you are interested in and select one pool the stock is from;
3. For the chromedriver in selenium, we need to download chromedriver.exe (download link: https://sites.google.com/a/chromium.org/chromedriver/home） and replace the path with your own path to chromedriver;
```
driver = webdriver.Chrome(executable_path = 'YOUR OWN PATH TO CHROMEDRIVER')
```






### References:

