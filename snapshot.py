import os
import yfinance as yf
import datetime
from datetime import date
todaydate=date.today()
#s
with open('ttm-squeeze/symbols.csv') as f:
    lines = f.read().splitlines()
    for symbol in lines:
        print(symbol)
        file=f"datasets/{format}.csv"
        if os.path.exists(file)==False:
            try:
                data = yf.download(symbol, start="2020-01-01", end=todaydate)
                data.to_csv("datasets/{}.csv".format(symbol))
            except:
                pass