import sys
import pybithumb
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time


form_class = uic.loadUiType(r'C:\Users\jmjwj\Desktop\bull.ui')[0]
tickers = ["BTC", "ETH", "BCH", "ETC"]


class Worker(QThread):
    finished = pyqtSignal(dict)
    def run(self):
        while True:
            data = {}

            for ticker in tickers :
                data[ticker] = self.get_market_infos(ticker)

            self.finished.emit(data)
            time.sleep(2)


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



class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.worker = Worker()
        self.worker.finished.connect(self.update_table_widjet)
        self.worker.start()

    @pyqtSlot(dict)
    def update_table_widjet(self,data):
        try:
            for ticker, infos in data.items():
                index = tickers.index(ticker)

                self.tablewidjet.setItem(index,0,QTableWidgetItem(ticker))
                self.tablewidjet.setItem(index,1,QTableWidgetItem(str(infos[0])))
                self.tablewidjet.setItem(index,2,QTableWidgetItem(str(infos[1])))
                self.tablewidjet.setItem(index,3,QTableWidgetItem(str(infos[2])))
        except:
            pass


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()