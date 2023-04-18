from data.repositories.e_wallet_repo import E_wallet_repo
from data.models.wallet import EWallet


class E_wallet_repo_impl(E_wallet_repo):

    def __init__(self):
        self.__entries: list[EWallet] = []
        self.count = 0

    def save(self, e_wallet: EWallet):
        wallet_not_found = e_wallet.get_id() == 0
        if wallet_not_found:
            e_wallet.set_id(self.count + 1)
            self.__entries.append(e_wallet)
            self.count += 1
        return e_wallet

    def find(self, id: EWallet):
        for i in self.__entries:
            if i.get_id() == id:
                return i
            else:
                return "Not found.."

    def     find_by_username_and_password(self, username, password):
        for i in self.__entries:
            if i.get_username() and i.get_password() == username and password:
                return i
            else:
                return "Not found.."
