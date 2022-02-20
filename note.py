import pybithumb
import numpy as np

def get_hpr_updown(ticker):
    try:
        df = pybithumb.get_ohlcv(ticker).loc['2018']
        df['ma5'] = df['close'].rolling(5).mean().shift(1)
        df['bull'] = df['ma5'] < df['open']

        df['target'] = df['open'] + ((df['high']-df['low'])*0.5).shift(1)
        df['ror'] = np.where((df['target'] < df['high']) & df['bull'], (df['close']-df['target']) / df['target'] , 1 )
        df['hpr_updown'] = df['ror'].cumprod()

        return df['hpr_updown'][-2]

    except : return 1



tickers = pybithumb.get_tickers()
hprs = []
for ticker in tickers:
    hpr = get_hpr_updown(ticker)
    hprs.append((ticker, hpr))

sorted_hprs = sorted(hprs, key = lambda x:x[1], reverse = True)

print(sorted_hprs[:5])


