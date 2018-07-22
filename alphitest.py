#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 21:57:39 2018

@author: roman
"""

# sudo python -m pip install alpha_vantage
# sudo python -m pip install pandas

import json
from pandas import *
from alpha_vantage.timeseries import TimeSeries
import sys

savdout = sys.stdout
fscock = open('out.log', 'w')
sys.stdout = fsock
print(update_all_prices(cd, '7ZXZNBI2F6TB79HK'))

def update_all_prices(company_dict, key):
    
    '''
    returns nothing
    '''
    
    for ticker in company_dict.keys():
        
        ts = TimeSeries(key, output_format = 'pandas')
        data, meta = ts.get_intraday(ticker)
        
        if data.shape[0] == 100:
            company_dict[ticker] = data.iat[99,4]

cd = {'VTR': 0, 'TXT': 0, 'AEE': 0, 'EQIX': 0, 'BLK': 0}

saveout = sys.stdout
fsock = open('out.log', 'w')
sys.stdout = fsock
print(update_all_prices(cd, '7ZXZNBI2F6TB79HK'))
sys.stdout = saveout
fsock.close