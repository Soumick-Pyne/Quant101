# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:05:30 2020

@author: User
"""
import yfinance as yf

data = yf.download("MSFT",start="2017-01-01",end="2020-04-24")

data_intra = yf.download("MSFT",period="1mo",interval="90m")



