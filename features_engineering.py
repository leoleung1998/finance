import pandas as pd
from sklearn import preprocessing
import requests
from functions import gain, loss
# Relative Strength Index
def rsi(stock):    
    # Create a list, fill first 14 values with 'None'
    rsi_list = [None for i in range(14)]
    # Change as an input
    stock = stock.Change
    
    # Calculating first RSI
    avg_gain = sum([i for i in stock[1:15] if i > 0])/14
    avg_loss = sum([abs(i) for i in stock[1:15] if i < 0])/14
    rs = avg_gain / avg_loss
    rsi = 100 - ( 100 / ( 1 + rs ))
    rsi_list.append(rsi)
    
    # Calculating following RSI's
    for i in range(15, len(stock)):
        avg_gain = (avg_gain * 13 + gain(stock[i]))/14
        avg_loss = (avg_loss * 13 + loss(stock[i]))/14
        rs = avg_gain / avg_loss
        rsi = 100 - ( 100 / ( 1 + rs ))
        rsi_list.append(rsi)
    
    return rsi_list   
 
# Moving Average Convergence/Divergence        
def macd(stock):
    exp1 = stock.close_price.ewm(span=12, adjust=False).mean()
    exp2 = stock.close_price.ewm(span=26, adjust=False).mean()
    macd = exp1-exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal
 
# Bollinger Bands    
def bollinger_bands(stock, window=240):
    rolling_mean = stock.close_price.rolling(window).mean()
    rolling_std = stock.close_price.rolling(window).std()
    upper_band = rolling_mean + (rolling_std*2)
    lower_band = rolling_mean - (rolling_std*2)
    return upper_band, lower_band
    
def ma5(stock):
    return stock.close_price.rolling(12).mean()
  
# Moving Average (21 days period)  
def ma15(stock):
    return stock.close_price.rolling(60).mean()
    
def momentum(data, n_days):
    m = [None for i in range(n_days)]    
    for i in range(len(data) - n_days):
        end = i + n_days
        m.append(data[i] - n_days)
    return m
