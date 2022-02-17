import sys

import pybithumb
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *


form_class = uic.loadUiType(r'C:\Users\jmjwj\Desktop\bull.ui')[0]
tickers = ["BTC", "ETH", "BCH", "ETC"]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tablewidjet.setItem(i,0,item)
            price, last_ma5, state = self.get_market_infos(ticker)
            self.tablewidjet.setItem(i,1,QTableWidgetItem(str(price)))
            self.tablewidjet.setItem(i,2,QTableWidgetItem(str(last_ma5)))
            self.tablewidjet.setItem(i,3,QTableWidgetItem(state))


    def get_market_infos(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        ma5 = df['close'].rolling(5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)

        state = None
        if price > last_ma5:
            state = '상승장'
        else : state = '하락장'

        return price, last_ma5, state


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
