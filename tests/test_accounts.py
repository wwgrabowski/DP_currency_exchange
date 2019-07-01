
from unittest import TestCase
from unittest.mock import patch
from python.accounts import BasicAccount, CreditAccount, DebetAccount, InterestZero


class TestAccounts(TestCase):

    def setUp(self):
        self.basic = BasicAccount('id_1', 1000, 'Wowo')
        self.credit = CreditAccount(self.basic)
        self.debet = DebetAccount(self.basic)

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

    def test_change_saldo_under_zero(self):
        self.assertRaises(ValueError, self.basic.change_saldo, -1200)

    @patch.object(InterestZero, 'get_interest')
    def test_add_interest(self, mock_get_interest):
        mock_get_interest.return_value = 100
        self.basic.add_interest()

        saldo = self.basic.saldo
        self.assertEqual(saldo, 1100)

    def test_get_owner(self):
        owner = self.basic.get_owner()
        self.assertEqual(owner, 'Wowo')

    def test_debet_account(self):
        id_before = self.basic.get_id()
        debet = DebetAccount(self.basic)
        id_after = debet.get_id()
        self.assertEqual(id_before, id_after)

    def test_credit_account(self):
        id_before = self.basic.get_id()
        credit = CreditAccount(self.basic)
        id_after = credit.get_id()
        self.assertEqual(id_before, id_after)

    def test_multiple_decorators(self):
        id_before = self.basic.get_id()
        credit_debet = CreditAccount(DebetAccount(self.basic))
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

    def test_debet_account_change_saldo(self):
        self.debet.change_saldo(-1500)
        saldo = self.debet.get_saldo()
        self.assertEqual(saldo, -500)

    def test_debet_account_overdebt(self):
        self.assertRaises(ValueError, self.credit.change_saldo, -2500)


