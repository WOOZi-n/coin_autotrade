import requests
import datetime

r= requests.get(r"https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitcoin = r.json()
print(bitcoin)
date = datetime.datetime.fromtimestamp(bitcoin["timestamp"]/1000)
print(date)
