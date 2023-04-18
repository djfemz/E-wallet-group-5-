from data.repositories.e_wallet_repo_impl import E_wallet_repo_impl
from dtos.requests.login_request import Login_request
from dtos.requests.register_request import Register_request
from services.e_wallet_service import E_wallet_service
from utils.mapper import Mapper

e_wallet: E_wallet_repo_impl


class E_wallet_service_impl(E_wallet_service):
    def register_user(self, request: Register_request):
        e_wallet.save(Mapper.map(request))
        return "Registration successful.."

    def integrate_card(self, card_number, cvv, expiry_date, first_name, last_name, password):
        pass

    def login(self, username, password):
        found_user = e_wallet.find_by_username_and_password(username, password)
        return "Welcome back" + found_user

    def add_money(self):
        pass

    def check_balance(self):
        pass

    def payment(self):
        pass
