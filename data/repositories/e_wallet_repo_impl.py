from data.repositories.e_wallet_repo import E_wallet_repo
from data.models.wallet import EWallet
from models import wallet


class E_wallet_repo_impl(E_wallet_repo):


    def __init__(self):
        self.__entries: list[EWallet] = []

        self.count = 0

    def save(self, e_wallet: EWallet) -> str:
        e_wallet.set_id(self.count + 1)
        self.__e_wallets.append(e_wallet)
        self.count = self.count + 1
        print(self.count)
        return e_wallet.get_first_name() + " " + e_wallet.get_last_name() + ", " + "your wallet has been created with" \
                                                                                   "username" + " " + e_wallet.get_userName()


    def find(self, userName) -> EWallet:
        for i in self.__e_wallets:
            if i.get_userName() == userName:
                return i



    def number_of_wallets(self) -> int:
        return self.count

