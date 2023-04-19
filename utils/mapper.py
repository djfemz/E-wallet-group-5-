from data.models.wallet import EWallet
from dtos.requests.register_request import Register_request


class Mapper:

    @staticmethod
    def map(request: Register_request):
        EWallet.set_last_name(request.get_last_name())
        EWallet.set_first_name(request.get_first_name())
        EWallet.set_username(request.get_user_name())
        EWallet.set_password(request.get_password())
        return EWallet

