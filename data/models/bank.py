import bank as bank
from bank.bank import Account


class bank:

    def __init__(self):
        self.__accounts: list[Account] = []

    def save(self, account):
        pass

    def find(self, cardNumber) -> Account:
        raise NotImplementedError

    def number_of_accounts(self) -> int:
        raise NotImplementedError
