import yfinance as yf
data=yf.download("SPY",start='2000-01-01',end='2020-05-31')
data.to_csv('s&p500.csv')