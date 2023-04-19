from dtos.requests.login_request import Login_request
from dtos.requests.register_request import Register_request


class E_wallet_service:
    def register_user(self, request: Register_request):
        raise NotImplementedError

    def integrate_card(self, card_number, cvv, expiry_date, first_name, last_name, password):
        raise NotImplementedError

    def login(self, username, password):
        raise NotImplementedError

    def add_money(self):
        raise NotImplementedError

    def check_balance(self):
        raise NotImplementedError

    def payment(self):
        raise NotImplementedError
