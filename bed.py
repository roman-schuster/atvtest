#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 23:30:45 2018

@author: roman
"""

import requests

API_URL = "https://www.alphavantage.co/query"

data = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "OLED",
    "outputsize": "compact",
    "datatype": "json",
    "apikey": "X856M5SJQGURS91D",
    }
    
response = requests.get(API_URL, data)

jsonrespo = response.json()

jsonrespo_no_meta = jsonrespo['Time Series (Daily)']
todaysies = jsonrespo_no_meta['2018-07-20']
print(todaysies)
