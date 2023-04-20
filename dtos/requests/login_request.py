class Login_request:
    def __init__(self, username, password):
        self.password = password
        self.username = username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        password+'a'
        return self.password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

