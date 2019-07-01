from unittest import TestCase
from python.interests import InterestZero, InterestFive, InterestTen


class TestInterests(TestCase):
    def setUp(self):
        self.saldo = 100

    def test_interest_zero(self):
        interest_zero = InterestZero()
        interest = interest_zero.get_interest(self.saldo)

        self.assertEqual(interest, 0)

    def test_get_interest(self):
        interest_five = InterestFive()
        interest = interest_five.get_interest(self.saldo)

        self.assertEqual(interest, 5)

    def test_interest_ten(self):
        interest_ten = InterestTen()
        interest = interest_ten.get_interest(self.saldo)

        self.assertEqual(interest, 10)
