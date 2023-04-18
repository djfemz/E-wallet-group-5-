
class E_wallet_repo:
    def save(self, e_wallet):
        raise NotImplementedError

    def find(self, id):
        raise NotImplementedError

    def find_by_username_and_password(self, username, password):
        raise NotImplementedError
