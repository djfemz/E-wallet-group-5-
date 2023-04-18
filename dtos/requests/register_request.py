class Register_request:
    def __init__(self, username, password, first_name, last_name):
        self.first_name = first_name,
        self.last_name = last_name,
        self.username = username,
        self.password = password

    def set_first_name(self, value):
        self.first_name = value

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, value):
        self.last_name = value

    def get_last_name(self):
        return self.last_name

    def set_user_name(self, value):
        self.username = value

    def get_user_name(self):
        return self.username

    def set_password(self, value):
        self.password = value

    def get_password(self):
        return self.password
