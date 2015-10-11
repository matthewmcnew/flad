from sample.stock import Stock


class StockCalculator():

    def __init__(self, stock_client):
        self._stock_client = stock_client

    def calculate(self, symbol):
        return Stock(symbol, self._stock_client.fetch('DOW'))