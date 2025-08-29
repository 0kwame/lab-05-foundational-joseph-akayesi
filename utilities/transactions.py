class Transactions:
    def __init__(self) -> None:
        self.__balance = 0
        self.__transactions = []

    def get_balance(self) -> int:
        return self.__balance

    def add_amount(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(f"amount must be greater than zero, got {amount}")
        self.__transactions.append(f"+{amount}")
        self.__balance += amount

    def withdraw_amount(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(f"amount must be greater than zero, got {amount}")
        if self.__balance - amount < 0:
            raise ValueError("insufficient funds for withdrawal")
        self.__transactions.append(f"-{amount}")
        self.__balance -= amount

    def get_last_transaction(self):
        return self.__transactions[-1]
    
    def get_summary(self):
        return f'balance: ${self.get_balance()}, last transaction: {self.get_last_transaction()}'



