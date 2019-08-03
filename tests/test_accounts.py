
from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock
from python.accounts import BasicAccount, CreditAccount, DebetAccount, InterestZero


class TestAccounts(TestCase):

    def setUp(self):
        class MockInterest:
            def __init__(self):
                self.interest = 0.1

            def get_interest(self, value):
                return value * self.interest

        self.basic = BasicAccount('id_1', 1000, 'Wowo', MockInterest)
        self.credit = CreditAccount(self.basic)
        self.debet = DebetAccount(self.basic, max_debet=1000)

    def test_get_id(self):
        basic_id = self.basic.get_id()
        self.assertEqual('id_1', basic_id)

    def test_get_saldo(self):
        saldo = self.basic.get_saldo()
        self.assertEqual(saldo, 1000)

    def test_change_saldo(self):
        self.basic.change_saldo(-200)
        current_saldo = self.basic.saldo
        self.assertEqual(current_saldo, 800)

    def test_change_saldo_to_zero(self):
        self.basic.change_saldo(-1000)
        current_saldo = self.basic.saldo
        self.assertEqual(current_saldo, 0)

    def test_change_saldo_under_zero(self):
        self.assertRaises(ValueError, self.basic.change_saldo, -1200)

    @patch.object(InterestZero, 'get_interest')
    def test_add_interest_call(self, mock_get_interest):
        mock_get_interest.return_value = 100
        self.basic.add_interest()

        saldo = self.basic.saldo
        self.assertEqual(saldo, 1100)

    def test_add_interest(self):
        self.basic.add_interest()

        saldo = self.basic.saldo
        self.assertEqual(saldo, 1100)

    def test_add_interest_to_zero(self):
        self.basic.saldo = 0
        self.basic.add_interest()

        saldo = self.basic.saldo
        self.assertEqual(saldo, 0)

    def test_add_interest_on_debet(self):
        self.debet.saldo = -200
        self.assertRaises(ValueError, self.debet.add_interest())
        saldo = self.debet.saldo
        self.assertEqual(saldo, -200)

    def test_get_owner(self):
        owner = self.basic.get_owner()
        self.assertEqual(owner, 'Wowo')

    def test_debet_account(self):
        id_before = self.basic.get_id()
        debet = DebetAccount(self.basic, 1000)
        id_after = debet.get_id()
        self.assertEqual(id_before, id_after)

    def test_credit_account(self):
        id_before = self.basic.get_id()
        credit = CreditAccount(self.basic)
        id_after = credit.get_id()
        self.assertEqual(id_before, id_after)

    def test_multiple_decorators(self):
        id_before = self.basic.get_id()
        credit_debet = CreditAccount(DebetAccount(self.basic, 1000))
        id_after = credit_debet.get_id()
        self.assertEqual(id_before, id_after)

    def test_get_credit_debt(self):
        debt = self.credit.get_credit_debt()
        self.assertEqual(debt, 0)

    def test_take_credit(self):
        self.credit.take_credit(1000)
        debt = self.credit.get_credit_debt()
        saldo = self.credit.get_saldo()

        self.assertEqual(debt, 1000)
        self.assertEqual(saldo, 2000)

    def test_take_zero_credit(self):
        self.assertRaises(ValueError, self.credit.take_credit(0))
        debt = self.credit.get_credit_debt()
        saldo = self.credit.get_saldo()

        self.assertEqual(debt, 0)
        self.assertEqual(saldo, 1000)

    def test_take_negative_credit(self):
        self.assertRaises(ValueError, self.credit.take_credit(-200))
        debt = self.credit.get_credit_debt()
        saldo = self.credit.get_saldo()

        self.assertEqual(debt, 0)
        self.assertEqual(saldo, 1000)

    def test_debet_account_change_saldo(self):
        self.debet.change_saldo(-1500)
        saldo = self.debet.get_saldo()
        self.assertEqual(saldo, -500)

    def test_debet_account_max_debt(self):
        self.debet.change_saldo(-2000)
        saldo = self.debet.get_saldo()
        self.assertEqual(saldo, -1000)

        self.assertRaises(ValueError, self.credit.change_saldo, -1)

    def test_debet_account_overdebt(self):
        self.assertRaises(ValueError, self.credit.change_saldo, -2500)

    def test_accept(self):
        id = '1'
        visitor = Mock()
        visitor.visit_product_id = MagicMock(return_value=id)
        product_id = self.basic.accept(visitor)

        visitor.visit_product_id.assert_called()
        self.assertEqual(id, product_id)
