import pybithumb
import time
import datetime

with open("bithumb.txt") as f:
    lines = f.readlines()
    con_key = lines[0].strip()
    sec_key = lines[1].strip()
    bithumb = pybithumb.Bithumb(con_key, sec_key)


def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    yesterday_high = yesterday["high"]
    yesterday_low = yesterday["low"]
    today_open = yesterday["close"]
    target = today_open + (yesterday_high - yesterday_low) * 0.5

    return target


def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw / float(sell_price)
    bithumb.buy_market_order(ticker, unit)


def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)


def get_yesterday_ma5(ticker):
    ohlcv = pybithumb.get_ohlcv(ticker)
    ma5 = ohlcv['close'].rolling(5).mean()
    return ma5[-2]


now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target = get_target_price("BTC")
ma5 = get_yesterday_ma5("BTC")

while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds = 10) :
            target = get_target_price("BTC")
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            sell_crypto_currency("BTC")

        current_price = pybithumb.get_current_price("BTC")

        if (current_price > target) and (current_price > ma5):
            buy_crypto_currency("BTC")


    except :
        print("에러발생")

    time.sleep(1)




