# import yfinance as yf
# data = yf.download('AAPL', start='2019-01-01', end='2025-01-01')
# print(data.head())


#Read Microsoft data and get historical market data
import yfinance as yf
import pandas as pd
import math

#Get historical market data
stock = yf.Ticker("VOO") 
market = yf.Ticker("VOO") 
hist = stock.history(period="1y")
hist_market = market.history(period="1y")
print(hist.head())

#Calculate daily returns for stock and market
daily_returns = hist['Close'].pct_change()
daily_returns_market = hist_market['Close'].pct_change()

#Calculate the standard deviation of daily returns for stock and market
std_dev = daily_returns.std()
std_dev_market = daily_returns_market.std()

#Calculate the Sharpe Ratio assuming a risk-free rate of 2%
rf_rate = 0.02 # 2% risk-free rate  
sharpe = (daily_returns.mean() - rf_rate)/std_dev * math.sqrt(252) # Annualize 

#Print the daily returns and standard deviations
print("Daily Returns: \n", daily_returns)
print("Standard Deviation of Daily Returns: \n", std_dev)
print("Sharpe Ratio of Daily Returns: \n", sharpe)
