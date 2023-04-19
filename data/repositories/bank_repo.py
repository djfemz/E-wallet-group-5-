from abc import ABC

from bank.bank import Account


class bank_repo:

    def save(self, account):
        pass

    def find(self, cardNumber) -> Account:
        raise NotImplementedError

    def number_of_accounts(self) -> int:
        raise NotImplementedError
