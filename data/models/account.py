class Account(CreditCard):

    def __init__(self, gender, NIN, BVN, email, address, first_name, last_name, dob):
        self.gender = gender,
        self.BVN = BVN,
        self.NIN = NIN,
        self.email = email,
        self.address = address,
        self.last_name = last_name,
        self.first_name = first_name,
        self.dob = dob

    def set_gender(self, value):
        self.gender = value

    def get_gender(self):
        return self.gender

    def set_bvn(self, value):
        self.BVN = value

    def get_bvn(self):
        return self.BVN

    def set_nin(self, value):
        self.NIN = value

    def get_nin(self):
        return self.NIN

    def set_email(self, value):
        self.email = value

    def get_email(self):
        return self.email

    def set_address(self, value):
        self.address = value

    def get_address(self):
        return self.address

    def set_last_name(self, value):
        self.last_name = value;

    def get_last_name(self):
        return self.last_name

    def set_first_name(self, value):
        self.first_name = value;

    def get_first_name(self):
        return self.first_name

    def set_dob(self, value):
        self.dob = value

    def get_dob(self):
        return self.dob

    def __str__(self):
        return f"""
                    ==========
                    gender: {self.gender}
                    BVN : {self.BVN}
                    NIN: {self.NIN}
                    email:{self.email}
                    address:{self.address}
                    last_name:{self.last_name}
                    first_name:{self.first_name}
                    dob:{self.dob}
                    ==========
                    """
