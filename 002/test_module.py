import unittest
from budget import Category


class Unittests(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.food = Category("Food")
        self.entertainment = Category("Entertainment")
        self.business = Category("Business")

    def test_deposit_no_description(self):
        self.food.deposit(45.56)
        actual = self.food.ledger[1]
        expected = {"amount": 45.56, "description": ""}
        self.assertEqual(
            actual, expected, 'Expected calling `deposit` method with no description to create a blank description.')

    def test_withdraw(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.ledger[1]
        expected = {"amount": -45.67,
                    "description": "milk, cereal, eggs, bacon, bread"}
        self.assertEqual(
            actual, expected, 'Expected `withdraw` method to create a specific object in the ledger instance variable')

    def test_withdraw_no_description(self):
        self.food.deposit(900, "deposit")
        good_withdraw = self.food.withdraw(45.67)
        actual = self.food.ledger[1]
        expected = {"amount": -45.67, "description": ""}
        self.assertEqual(
            actual, expected, 'Expected `withdraw` method with no description to create a blank description.')
        self.assertEqual(good_withdraw, True,
                         'Expected `withdraw` method to return `True`.')

    def test_get_balance(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual = self.food.get_balance()
        expected = 854.33
        self.assertEqual(actual, expected, 'Expected balance to be 854.33')

    def test_transfer(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, ceral, eggs, bacon, bread")
        transfer_amount = 20
        print("food", self.food.ledger)
        print("entertainment", self.entertainment.ledger)
        # pprint("ent", self.entertainment.ledger)
        food_balance_before = self.food.get_balance()
        entertainment_balance_before = self.entertainment.get_balance()
        print("food_balance_before", food_balance_before)
        print("entertainment_balance_before", entertainment_balance_before)
        good_transfer = self.food.transfer(transfer_amount, self.entertainment)
        food_balance_after = self.food.get_balance()
        entertainment_balance_after = self.entertainment.get_balance()
        actual = self.food.ledger[2]
        expected = {"amount": -transfer_amount,
                    "description": "Transfer to Entertainment"}
        self.assertEqual(good_transfer, True,
                         'Expected `transfer` method to return `True`')
        self.assertEqual(food_balance_before - food_balance_after, transfer_amount,
                         'Expected `transfer` method to reduce balance in food object.')
        self.assertEqual(entertainment_balance_after - entertainment_balance_before, transfer_amount,
                         'Expected `transfer` method to increase balance in entertainment object.')
        actual = self.entertainment.ledger[0]
        expected = {"amount": transfer_amount,
                    "description": "Transfer from Food"}
        self.assertEqual(
            actual, expected, 'Expected `transfer` method to create a specific ledger item in entertainment object.')


if __name__ == "__main__":
    unittest.main()
