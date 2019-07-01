
from unittest import TestCase
from python.accounts import BasicAccount, CreditAccount, DebetAccount


class TestAccounts(TestCase):

    def setUp(self):
        self.basic = BasicAccount('id_1', 1000, 'Wowo')

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

    def test_add_interest(self):
        self.basic._interest = 0.1
        self.basic.add_interest()
        current_saldo = self.basic.saldo
        self.assertEqual(current_saldo, 1100)

    def test_change_interest(self):
        pass

    def test_get_owner(self):
        owner = self.basic.getOwner()
        self.assertEqual(owner, 'Wowo')
