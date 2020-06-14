# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:49:11 2020

@author: User
"""

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

key_path = "E:\\quant course\\apha_key.txt"

#extracting data from a single ticker
ts = TimeSeries(key=open(key_path,'r').read(),output_format='pandas')
data = ts.get_daily(symbol="EURUSD",outputsize='compact')[0]
data.columns = ['open','high','low','close','volume']
data = data.iloc[::-1]

all_tickers = ["AAPL","MSFT","CSCO","AMZN","GOOG","FB"]
close_prices = pd.DataFrame()
api_call_count = 0
start_time = time.time()
for ticker in all_tickers:
    ts = TimeSeries(key=open(key_path,'r').read(),output_format='pandas')
    data = ts.get_intraday(symbol=ticker,interval='1min',outputsize='compact')[0]
    api_call_count+=1
    data.columns = ['open','high','low','close','volume']
    data = data.iloc[::-1]
    close_prices[ticker] = data['close']
    if api_call_count==5:
        api_call_count=0
        time.sleep(60-(time.time()-start_time))
