import pybithumb
import time
import datetime

orderbook = pybithumb.get_orderbook("BTC")
ms = int(orderbook["timestamp"])
time = datetime.datetime.fromtimestamp(ms/1000)
print(time)