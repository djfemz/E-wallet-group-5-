from models import wallet
from models.wallet import EWallet


class E_wallet_repo:
    def save(self, e_wallet):
        raise NotImplementedError


    def find(self, username) -> EWallet:
        raise NotImplementedError

    def number_of_wallets(self) -> int:
        raise NotImplementedError
