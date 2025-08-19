class Transactions:
    def __init__(self) -> None:
        self.__total_amount = 0

    def get_total_amount(self) -> int:
        return self.__total_amount

    def add_amount(self, amount: int) -> None:
        self.__total_amount += amount

    def withdraw_amount(self, amount: int) -> None:
        self.__total_amount -= amount

