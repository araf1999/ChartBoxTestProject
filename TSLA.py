import yfinance as yf

tesla = yf.Ticker('TSLA')
teslaData= tesla.history(period="60d", interval="15m")

#Finding RSI parameter for every row of our data
def RSI(data, window=14, adjust=False):
    delta = data['Close'].diff(1).dropna()
    loss = delta.copy()
    gains = delta.copy()
    gains[gains < 0] = 0
    loss[loss > 0] = 0
    gain_ewm = gains.ewm(com=window - 1, adjust=adjust).mean()
    loss_ewm = abs(loss.ewm(com=window - 1, adjust=adjust).mean())
    RS = gain_ewm / loss_ewm
    RSI = 100 - 100 / (1 + RS)
    return RSI

#Finding start point of trade
Rlist = [rsi for rsi in RSI(teslaData)]
for row in RSI(teslaData):
    if row<30:
        print('Log in .......')
        start = teslaData.iloc[Rlist.index(row)]
        print(start)
        break

#Finding end point of trade
for Row in RSI(teslaData):
    if Row>50 and Rlist.index(Row)>Rlist.index(row):
        print('Log out .......')
        end = teslaData.iloc[Rlist.index(Row)]
        print(end)
        break