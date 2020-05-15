from alpha_vantage.timeseries import TimeSeries
import alpha_vantage_parameters
import pandas as pd
import time
import json
from datetime import datetime


class StreamQuotes(TimeSeries):
    """
    gets the intraday quotes for sp500, vix.
    returns a dictionary with each symbol as key
    has intraday for past week when on_stock_list() run on interval="1min", outputsize="full"
    returns a dictionary with each symbol as key, datafram as value.
    This dataframe is intraday and has format that can be seen on alphavantage
    """

    def on_stock(self, symbol, interval="60min", outputsize="compact"):
        # returns dataframe of single stock for current intraday quotes
        d, meta = self.get_intraday(symbol=symbol, interval=interval, outputsize=outputsize)
        #df = pd.DataFrame.from_dict(d, orient='index')
        print(d)
        return d

    def on_stock_list(self, symbols, interval="60min", outputsize="compact"):
        data = {}
        for s in symbols:
            data[s] = self.on_stock(s, interval, outputsize)
            #time.sleep(15) #to circumvent alpharad limitter of 5 calls per minute, we make 4 calls per minute
        return data

def save_to_file(data, data_filename):
    with open(data_filename, 'w') as fp:
        json.dump(data, fp)

if __name__ == "__main__":
    ts = StreamQuotes(key=alpha_vantage_parameters.API_KEY)
    output = ts.on_stock_list(symbols=["SPX", "VIX"],interval="1min",outputsize="full")
    today = str(datetime.today().strftime("%d-%m-%Y"))
    print(today)
    save_to_file(output, "sproj\\data\\financial\\"+today+".json")
    #print(output["APPL"])
