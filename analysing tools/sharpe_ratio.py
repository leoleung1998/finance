import yfinance as yf
import pandas as pd
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
period=365
## getting the market data of cryptocurrencies on yahoo finance
response=requests.get("https://finance.yahoo.com/cryptocurrencies")
soup=BeautifulSoup(response.text,features='lxml')
results=soup.find_all('a',{"data-test":"quoteLink"})
tickers=[]
for i in results:
    tickers.append(i.text)
## set period to max to get all available data of BTC
df_all=yf.Ticker('BTC-USD').history(period='max').reset_index()[['Date','Open']]
df_all=df_all.rename(columns={'Open':'BTC-USD'})
for i in range(1,len(tickers)):
    df=yf.Ticker(tickers[i]).history(period='max').reset_index()[['Date','Open']]
    df=df.rename(columns={'Open':tickers[i]})
    df_all=df_all.merge(df,on='Date',how='left')
df_all['Date']=pd.to_datetime(df_all.Date)
df_all.set_index('Date',inplace=True)
## plot rolling sharpe ratio
for i in [365,90,30]:
    returns=df_all.pct_change(i)
    voliatility=returns.rolling(i).std()
    sharpe_ratio=returns/voliatility
    token_sr={k: v for k, v in sorted(sharpe_ratio.mean().to_dict().items(), key=lambda item: item[1],reverse=True)}
    top_tokens=list(token_sr.keys())[:10]
    sharpe_ratio[top_tokens][-180:].plot()
    print(f"{i} Days \n Rolling Sharpe Ratio" ,list(token_sr.items())[:10])
    plt.plot(f'{i} Days rolling SR for top 10 tokens.jpg')
plt.show()