
from unittest import TestCase
from python.currency_exchange import CurrencyExchange


class TestCurrencyExchange(TestCase):

    def setUp(self):
        self.exchange_1 = CurrencyExchange()

    def test_init(self):
        self.assertEqual(self.exchange_1.exchange_id, 1)


