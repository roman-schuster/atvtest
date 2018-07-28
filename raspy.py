#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 23:30:45 2018
@author: roman
"""

import requests

API_URL = "https://www.alphavantage.co/query"

list_of_requests = []
tickers = ['ALB', 'PCG', 'KMB', 'LYB', 'WBA']

for ticker in tickers:

    data = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": "5YAOW9ZPOB6F3VTB"
        }
    
    list_of_requests.append(data)
    
for request in list_of_requests:
    response = requests.get(API_URL, request)
    jsonrespo = response.json()
    jsonrespo_no_meta = jsonrespo['Time Series (Daily)']
    todaysies = jsonrespo_no_meta['2018-07-20']
    print(todaysies)
