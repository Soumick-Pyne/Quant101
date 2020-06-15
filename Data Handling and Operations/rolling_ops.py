# =============================================================================
# Import OHLCV data and perform basic data operations
# =============================================================================

# Import necesary libraries
import datetime as dt
import yfinance as yf
import pandas as pd

# Download historical data for required stocks
tickers = ["MSFT","AMZN","AAPL","CSCO","IBM","FB"]

start = dt.datetime.today()-dt.timedelta(3650)
end = dt.datetime.today()
close_prices = pd.DataFrame() # empty dataframe which will be filled with closing prices of each stock

# looping over tickers and creating a dataframe with close prices
for ticker in tickers:
    close_prices[ticker] = yf.download(ticker,start,end)["Adj Close"]


# Rolling mean and standard deviation
daily_return.rolling(window=20).mean() # simple moving average
daily_return.rolling(window=20).std()

daily_return.ewm(span=20,min_periods=20).mean() # exponential moving average
daily_return.ewm(span=20,min_periods=20).std()




