from data.models.credit_card import CreditCard


class EWallet:
    def __init__(self):
        self.credit_cards: list[CreditCard] = []
        self.first_name = str
        self.last_name = str
        self.password = str
        self.userName = str
        self.id = int
        self.username = str

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_first_name(self, name):
        self.first_name = name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, name):
        self.last_name = name

    def get_last_name(self):
        return self.last_name

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def str(self):
        return f"""
                     ==========
                     id: {self.id}
                     first_name: {self.first_name}
                     last_name: {self.last_name}
                     password:{self.password}
                     user_name:{self.username}

                     ==========
                     """




