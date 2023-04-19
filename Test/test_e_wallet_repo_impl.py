from unittest import TestCase

from models import wallet
from models.wallet import EWallet
from repositories.e_wallet_repo import E_wallet_repo
from repositories.e_wallet_repo_impl import E_wallet_repo_impl


class Test_e_wallet(TestCase):
    wallet: EWallet
    e_wallet: E_wallet_repo

    def setUp(self) -> None:
        self.wallet = EWallet()
        self.wallet.set_first_name("felix")
        self.wallet.set_last_name("ezeike")
        self.wallet.set_userName("felixezeike")
        self.wallet.set_password("0000")
        self.e_wallet = E_wallet_repo_impl()

    def test_wallet_can_be_created(self):
        self.e_wallet.save(self.wallet)
        self.assertEqual(1, self.e_wallet.number_of_wallets())
        self.assertEqual(1, self.wallet.get_id())

    def test_multiple_wallets_can_be_stored(self):
        self.e_wallet.save(self.wallet)
        self.assertEqual(1, self.wallet.get_id())
        self.wallet2 = EWallet()
        self.wallet2.set_first_name("felix2")
        self.wallet2.set_last_name("ezeike2")
        self.wallet2.set_userName("felixezeike2")
        self.wallet2.set_password("1111")
        self.e_wallet.save(self.wallet2)
        self.assertEqual(2, self.e_wallet.number_of_wallets())
        self.assertEqual(2, self.wallet2.get_id())

    def test_find(self):
        self.e_wallet.save(self.wallet)
        self.wallet2 = EWallet()
        self.wallet2.set_first_name("felix2")
        self.wallet2.set_last_name("ezeike2")
        self.wallet2.set_userName("felixezeike2")
        self.wallet2.set_password("1111")
        self.e_wallet.save(self.wallet2)
        self.assertEqual(2, self.e_wallet.number_of_wallets())
        self.assertEqual(2, self.wallet2.get_id())
        self.assertEqual("felix2", self.e_wallet.find("felixezeike2").get_first_name())
