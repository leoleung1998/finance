import pandas as pd
import matplotlib.pyplot as plt
from pyalgotrade import strategy
from pyalgotrade.feed import csvfeed
from pyalgotrade.barfeed import quandlfeed,yahoofeed
class bhStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(bhStrategy, self).__init__(feed)
        self.instrument =instrument
        self.setUseAdjustedValues(True)
        self.position = None
    def onEnterOk(self, position):
        self.info(f"{position.getEntryOrder().getExecutionInfo()}")
    def onBars(self,bars):
        bar = bars[self.instrument]
        if self.position == None:
            close=bar.getClose()
            broker=self.getBroker()
            cash=broker.getCash()
            quantity=cash/close
            self.position= self.enterLong(self.instrument, quantity)



feed=yahoofeed.Feed()
feed.addBarsFromCSV('spy','s&p500.csv')

s=bhStrategy(feed,'spy')
s.run()
pv=s.getBroker().getEquity()+s.getBroker().getCash()
print(pv)