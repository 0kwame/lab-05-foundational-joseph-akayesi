class Transactions:
    def __init__(self) -> None:
        self.balance = 0

    def get_total_amount(self) -> int:
        return self.balance

    def add_amount(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(f"amount must be greater than zero, got {amount}")
        self.balance += amount

    def withdraw_amount(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(f"amount must be greater than zero, got {amount}")
        if self.balance - amount < 0:
            raise ValueError("insufficient funds for withdrawal")
        self.balance -= amount



