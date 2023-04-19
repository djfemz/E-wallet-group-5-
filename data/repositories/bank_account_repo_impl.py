from data.models.account import Account
from data.repositories.credit_card_repo import Bank_account


class card_repo_impl(Bank_account):
    def __init__(self):
        self.__entries: list[Account] = []
        self.count = 0

    def save(self, accounts):
        credit_not_saved = accounts.get_id() == 0
        if credit_not_saved:
            accounts.set_id(self.count + 1)
            self.__entries.append(accounts)
            self.count += 1
        return accounts

    def find(self, id):
        for i in self.__entries:
            if i.get_id() == id:
                return i
            