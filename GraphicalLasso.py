#Implement the vanilla Graphical Lasso algorithm; more tweaks to follow soon;
import csv
import numpy as np


from urllib import request

#retrieve data for JPmorgan, Goldman Sachs, Morgan Stanley, Deutsche Bank, Citigroup, Barclays, UBS, Lazard and Wells Fargo
#a collection of IB and Tech firms tickers
tickers = ['JPM','GS','MS','DB','C','BCS', 'WFC', 'MSFT','AAPL','IBM', 'AMZN']

for t in tickers:
    #for each ticker, get the data from 2014 to 2015 todate
    data = request.urlopen("http://real-chart.finance.yahoo.com/table.csv?s=%s&d=9&e=31&f=2015&g=d&a=4&b=4&c=1999&ignore=.csv"%t)
    csv = str(data.read()).strip("b'").split("\\n")
    #write data to file
    f = open("%s_data.csv"%t,"w")
    for row in csv:
        #get trading price data by preprocessing -- Adj Close Price
        if row:
            vol = row.split(',')[5]
            f.write(vol +"\n")
    f.close()

#initialize W = S. The diagonal of W shall remain unchanged always:

#initialize datamatrix: row: price; column: ticker
datamatrix=np.zeros((4152, len(tickers)))

#looping over each ticker
cnt = 0
for t in tickers:
    with open("%s_data.csv"%t, 'rb') as f:
        list_cur = f.read().splitlines()
        list = np.asfarray(list_cur[1:])
        #truncate so that it does not contain the column header
        mean = np.mean(list)
        std = np.std(list)
        datamatrix[:,cnt] = [(x-mean)/std for x in list]
    cnt+=1

#calculate covariance:
datamatrix=datamatrix.T
S=np.cov(datamatrix)
W=S







        
        

