# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:31:16 2020

@author: User
"""
import datetime as dt
import yfinance as yf
import pandas as pd

stocks = ["AMZN","MSFT","INTC","GOOG","INFY.NS","3988.HK"]

start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()

cl_price = pd.DataFrame() #creating an empty dataframe

#looping over tickers and creating a dataframe with closing prices
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)['Adj Close']
    
ohlcv_data = {}

for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker,start,end)


ohlcv_data["MSFT"]["Open"]