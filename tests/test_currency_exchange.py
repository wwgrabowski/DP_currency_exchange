
from unittest import TestCase
from python.currency_exchange import CurrencyExchange


class TestCurrencyExchange(TestCase):

    def setUp(self):
        self.exchange_1 = CurrencyExchange()

    def test_init(self):
        self.assertEqual(self.exchange_1.exchange_id, 1)

    def test_get_exchange_id(self):
        pass

    def test_store_operation(self):
        pass

    def test_get_exchange_history(self):
        pass

    def test_execute_operations(self):
        pass

    def test_get_exchange_product_by_id(self):
        pass

    def test_get_exchange_products(self):
        pass
