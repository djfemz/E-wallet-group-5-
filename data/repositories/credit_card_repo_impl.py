from abc import ABC

from data.models.credit_card import CreditCard
from data.repositories.credit_card_repo import Card_Interface


class card_repo_impl(Card_Interface):
    def __init__(self):
        self.__entries: list[CreditCard] = []
        self.count = 0

    def save(self, creditCard):
        credit_not_saved = creditCard.get_id() == 0
        if credit_not_saved:
            creditCard.set_id(self.count + 1)
            self.__entries.append(creditCard)
            self.count += 1
        return creditCard

    def find(self, id):
        for i in self.__entries:
            if i.get_id() == id:
                return i
