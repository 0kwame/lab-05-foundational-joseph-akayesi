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
        self.assertEqual(self.t.get_total_amount(), 100, "Should be 20")

    def test_withdraw_amount(self):
        self.t.add_amount(200)
        self.t.withdraw_amount(120)
        self.assertEqual(self.t.get_total_amount(), 80, "Should be 80")