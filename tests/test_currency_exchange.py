
from unittest import TestCase
from unittest.mock import Mock, MagicMock
from python.currency_exchange import CurrencyExchange


class TestCurrencyExchange(TestCase):

    def setUp(self):
        self.exchange_1 = CurrencyExchange()

    def test_init(self):
        self.assertEqual(self.exchange_1.exchange_id, 1)

    def test_get_exchange_id(self):
        self.assertEqual(1, self.exchange_1.get_exchange_id())

    def test_store_operation(self):
        operation = Mock()

        self.assertEqual(0, len(self.exchange_1._exchange_operations))
        self.exchange_1.store_operation(operation)
        self.exchange_1.store_operation(operation)
        self.assertEqual(2, len(self.exchange_1._exchange_operations))

    def test_get_exchange_history(self):
        self.exchange_1._exchange_history.append('hist')
        result = ['hist']

        history = self.exchange_1.get_exchange_history()
        self.assertEqual(result, history)

    def test_execute_operations(self):
        command = Mock()
        command.execute = MagicMock()

        self.exchange_1._exchange_operations = [command, command]
        self.exchange_1.execute_operations()

        self.assertEqual(2, command.execute.call_count)
        operations = self.exchange_1._exchange_operations
        self.assertEqual([], operations)
        self.assertEqual([command, command], self.exchange_1._exchange_history)

    def test_get_exchange_product_by_id(self):
        product = Mock()
        self.exchange_1._exchange_products['id'] = product

        gathered_product = self.exchange_1.get_exchange_product_by_id('id')
        self.assertEqual(product, gathered_product)

    def test_get_exchange_product_by_id_exception(self):
        self.assertRaises(KeyError,
                          self.exchange_1.get_exchange_product_by_id('id'))

    def test_get_exchange_products(self):
        product = Mock()
        self.exchange_1._exchange_products['id'] = product
        result = {'id': product}

        products = self.exchange_1.get_exchange_products()
        self.assertEqual(result, products)
