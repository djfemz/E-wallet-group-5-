class CreditCard:
    def __init__(self, id, card_number, balance, cvv, expiry_date, first_name, last_name, dob):
        self.id = id,
        self.card_number = card_number,
        self.balance = balance,
        self.cvv = cvv,
        self.expiry_date = expiry_date,
        self.first_name = first_name,
        self.last_name = last_name,
        self.dob = dob

    def card_number(self, value):
        self.card_number = value

    def get_card_number(self):
        return self.card_number

    def set_balance(self, value):
        self.balance = value

    def get_balance(self):
        return self.balance

    def set_cvv(self, value):
        self.balance = value

    def get_cvv(self):
        return self.cvv

    def set_expiry_date(self, value):
        self.expiry_date = value

    def get_expiry_date(self):
        return self.expiry_date

    def set_first_name(self, value):
        self.first_name = value

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, value):
        self.last_name = value;

    def get_last_name(self):
        return self.last_name

    def set_dob(self, value):
        self.dob = value

    def set_id(self, value):
        self.id = value

    def get_id(self):
        return self.id
