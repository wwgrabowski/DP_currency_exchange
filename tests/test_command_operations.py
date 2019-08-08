from unittest import TestCase
from unittest.mock import Mock, MagicMock
from python.command_operations import AddProduct, Deposit, Withdraw, Transfer, AddInterest, was_executed, Command


class TestCommandOperations(TestCase):

    def setUp(self):
        pass

    def test_id_generation(self):
        Command._id_generator = 0
        mock_product = Mock()
        deposit = Deposit(mock_product, 100)
        withdraw = Withdraw(mock_product, 100)

        deposit_id = deposit.get_id()
        withdraw_id = withdraw.get_id()

        self.assertEqual(deposit_id, 1)
        self.assertEqual(withdraw_id, 2)

    def test_add_product(self):
        mock_exchange = Mock()
        mock_exchange._exchange_products = dict()
        mock_product = Mock()
        mock_product.get_id = MagicMock(return_value='id')

        add_product = AddProduct(mock_exchange, mock_product)
        add_product.execute()

        mock_product.get_id.assert_called()
        self.assertTrue(mock_exchange._exchange_products['id'])

    def test_deposit(self):
        product = Mock()
        product.change_saldo = MagicMock()
        deposit = Deposit(product, 100)
        deposit.execute()

        product.change_saldo.assert_called()

    def test_withdraw(self):
        product = Mock()
        product.change_saldo = MagicMock()
        withdraw = Withdraw(product, 100)
        withdraw.execute()

        product.change_saldo.assert_called()

    def test_transfer(self):
        src_product = Mock()
        src_product.change_saldo = MagicMock()
        dst_product = Mock()
        dst_product.change_saldo = MagicMock()

        transfer = Transfer(src_product, dst_product, 100)
        transfer.execute()

        src_product.change_saldo.assert_called()
        dst_product.change_saldo.assert_called()

    def test_add_interest(self):
        account = Mock()
        account.add_interest = MagicMock()
        add_interest = AddInterest(account)
        add_interest.execute()

        account.add_interest.assert_called()

    def test_was_executed_wrapper(self):

        class MockCommand:
            def __init__(self):
                self.executed = False

            @was_executed
            def execute(self):
                pass

        mock_command = MockCommand()
        mock_command.execute()

        self.assertTrue(mock_command.executed)
        self.assertRaises(Exception, mock_command.execute())

