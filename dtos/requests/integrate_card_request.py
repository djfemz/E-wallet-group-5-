class Integrate_card_request:
    def __init__(self, card_number, cvv, expiry_date, first_name, last_name, password):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def set_card_number(self, value):
        self.card_number = value

    def get_card_number(self):
        return self.card_number

    def set_cvv(self, value):
        self.cvv = value

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
        self.last_name = value

    def get_last_name(self):
        return self.last_name

    def set_password(self, value):
        self.last_name = value

    def get_password(self):
        return self.last_name
