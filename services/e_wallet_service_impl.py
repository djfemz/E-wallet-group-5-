from data.repositories.e_wallet_repo_impl import E_wallet_repo_impl
from dtos.register_request import Register_request
from services.e_wallet_service import E_wallet_service
from utils.mapper import Mapper

e_wallet: E_wallet_repo_impl


class E_wallet_service_repo(E_wallet_service):
    def register_user(self, request: Register_request):
        e_wallet.save(Mapper.map(request))
        return "Registration successful.."

    def integrate_card(self, card_number, cvv, expiry_date, first_name, last_name, password):
        pass

    def login(self, password, username):
        pass

    def add_money(self):
        pass

    def check_balance(self):
        pass

    def transfer(self):
        pass
