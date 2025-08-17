import unittest
from utilities import Transactions

class TestTransactions(unittest.TestCase):
    def __init__(self, methodName='runTest'):  
        super().__init__(methodName)  

    def setUp(self):
        """Run before every test"""
        self.t = Transactions()

    def test_add_amount(self):
        self.t.add_amount(100)
        self.assertEqual(self.t.get_total_amount(), 100)

    def test_add_negative_amount_raises(self):
        amount = -100
        with self.assertRaises(ValueError) as cm:
            self.t.add_amount(amount)
        self.assertEqual(str(cm.exception), f"amount must be greater than zero, got {amount}")

    def test_add_zero_amount_raises(self):
        amount = 0
        with self.assertRaises(ValueError) as cm:
            self.t.add_amount(amount)
        self.assertEqual(str(cm.exception), f"amount must be greater than zero, got {amount}")

    def test_withdraw_amount(self):
        self.t.add_amount(200)
        self.t.withdraw_amount(120)
        self.assertEqual(self.t.get_total_amount(), 80)

    def test_withdraw_zero_amount_raises(self):
        amount = 0
        with self.assertRaises(ValueError) as cm:
            self.t.withdraw_amount(amount)
        self.assertEqual(str(cm.exception), f"amount must be greater than zero, got {amount}")

    def test_withdraw_more_than_balance_raises(self):
        self.t.add_amount(200)

        with self.assertRaises(ValueError) as cm:
            self.t.withdraw_amount(250)
        self.assertEqual(str(cm.exception), "insufficient funds for withdrawal")

