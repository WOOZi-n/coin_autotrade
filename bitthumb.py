import pybithumb

def bull_market(ticker):
    data = pybithumb.get_ohlcv(ticker)
    price = pybithumb.get_current_price(ticker)
    ma5 = data['close'].rolling(5).mean()
    last_ma5 = ma5[-2]

    if last_ma5 < price:
        return True
    else:
        return False


tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker,"상승장")
    else:
        print(ticker,"하락장")
