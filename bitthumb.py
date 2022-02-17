import pybithumb

con_key = "e628e625d8c195f0529772e8f30998e2"
sec_key = "ab4295abd375e31e60d3d38453354236"

bithumb = pybithumb.Bithumb(con_key, sec_key)

krw = bithumb.get_balance("BTC")[2]
orderbook = bithumb.get_orderbook("BTC")
asks = orderbook["asks"]
sell_price = asks[0]['price']
unit = krw/float(sell_price)
order = bithumb.buy_market_order("BTC", unit)
print(order)