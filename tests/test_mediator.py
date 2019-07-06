from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from python.mediator import ConcreteMediator, Withdraw, Deposit


class TestConcreteMediator(TestCase):

    def setUp(self):
        self.exchange_1 = Mock()
        self.exchange_2 = Mock()

        self.mediator = ConcreteMediator(self.exchange_1, self.exchange_2)

    @patch('python.mediator.Deposit')
    @patch('python.mediator.Withdraw')
    def test_transfer(self, mock_withdraw, mock_deposit):
        account_1 = Mock()
        account_2 = Mock()

        self.exchange_1.get_exchange_product_by_id = MagicMock(return_value=account_1)
        self.exchange_2.get_exchange_product_by_id = MagicMock(return_value=account_2)

        mock_withdraw.return_value = Mock()
        mock_deposit.return_value = Mock()

        self.exchange_1.execute_operation = MagicMock()
        self.exchange_2.execute_operation = MagicMock()

        self.mediator.transfer('src', 'dst', 100)

        self.exchange_1.get_exchange_product_by_id.assert_called()
        self.exchange_2.get_exchange_product_by_id.assert_called()
        self.exchange_1.execute_operation.assert_called()
        self.exchange_2.execute_operation.assert_called()

