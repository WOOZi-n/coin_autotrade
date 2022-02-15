from pandas import Series, DataFrame

data = {"open": [737, 750, 770], "high": [755, 780, 770], "low": [700, 710, 750], "close": [750, 770, 730]}
date = ["2018-01-01", "2018-01-02", "2018-01-03"]
df = DataFrame(data, index = date)

data2 = Series([55, 70, 20], index = date)
df["volatility"] = data2
print(df)