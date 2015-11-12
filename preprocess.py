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

