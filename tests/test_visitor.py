from unittest import TestCase
from unittest.mock import Mock
from python.visitor import ExchangeVisitor
from python.accounts import BasicAccount
from python.currency_exchange import CurrencyExchange


class TestVisitor(TestCase):

    def setUp(self):
        self.visitor = ExchangeVisitor()
        self.basic = BasicAccount('id', 100, 'Wowo')
        self.exchange = CurrencyExchange()

    def test_visit_exchange_history(self):
        history = [Mock(), Mock()]
        self.exchange._exchange_history = history
        exchange_history = self.exchange.accept(self.visitor)
        self.assertEqual(history, exchange_history)

    def test_visit_product_id(self):
        id = self.basic.accept(self.visitor)
        self.assertEqual('id', id)
