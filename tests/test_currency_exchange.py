
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
        command.get_id = MagicMock(side_effect=['1', '2'])
        command.execute = MagicMock()

        self.exchange_1._exchange_operations = [command, command]
        self.exchange_1.execute_operations()

        self.assertEqual(2, command.execute.call_count)
        operations = self.exchange_1._exchange_operations
        self.assertEqual([], operations)
        self.assertEqual(['1', '2'], self.exchange_1._exchange_history)

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

    def test_execute_operation(self):
        command = Mock()
        command.get_id = MagicMock(return_value='id')
        command.execute = MagicMock()

        self.exchange_1.execute_operation(command)
        command.execute.assert_called()
        self.assertEqual(['id'], self.exchange_1._exchange_history)

    def test_exchange_transfer(self):
        mock_mediator = Mock()
        self.exchange_1.mediator = mock_mediator
        mock_mediator.transfer = MagicMock()

        self.exchange_1.exchange_transfer('src', 'dst', 100)
        mock_mediator.transfer.assert_called()

    def test_exchange_transfer_exception(self):
        self.assertRaises(AttributeError, self.exchange_1.exchange_transfer('src', 'dst', 100))

    def test_accept(self):
        history = ['1']
        visitor = Mock()
        visitor.visit_exchange_history = MagicMock(return_value=history)
        exchange_history = self.exchange_1.accept(visitor)

        visitor.visit_exchange_history.assert_called()
        self.assertEqual(history, exchange_history)

