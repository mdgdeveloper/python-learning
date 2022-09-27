class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, value, description=""):
        self.ledger.append({"amount": value, "description": description})

    def withdraw(self, value, description=""):
        if (self.get_balance() - value >= 0):
            self.ledger.append({
                "amount": -value,
                "description": description
            })
            return True

    def get_balance(self):
        # Recorrer el array y sumar los amounts
        amount = 0
        for x in self.ledger:
            amount = amount + x["amount"]
        return (amount)

    def transfer(self, amount, otherBudget):
        withdraw = self.withdraw(amount, f"Transfer to {otherBudget.category}")
        if (withdraw):
            otherBudget.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False


def create_spend_chart(categories):
    return True
