# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:07:24 2020

@author: User
"""

from yahoofinancials import YahooFinancials

ticker = "MSFT"
#creating object
yahoo_financials = YahooFinancials(ticker)

data = yahoo_financials.get_historical_price_data("2018-04-24","2020-04-24","daily")

