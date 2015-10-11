import unittest
import mock
from sample.stock import Stock

from sample.stock_calculator import StockCalculator
from sample.stock_client import StockClient


class StockCalculatorTests(unittest.TestCase):

    @mock.patch.object(StockClient, 'fetch', autospec=True)
    def test_add_value(self, mock_fetch):
        mock_fetch.return_value = 22
        stock_client = StockClient()
        stock_calculator = StockCalculator(stock_client)

        dow = stock_calculator.calculate("DOW")

        self.assertIsInstance(dow, Stock)
        self.assertEqual(dow.symbol, "DOW")
        self.assertEqual(dow.price, 22)

        mock_fetch.assert_called_with(stock_client, "DOW")