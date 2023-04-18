
class EwalletRepo:
    def save(self, ewallet):
        raise NotImplementedError

    def find(self, id):
        raise NotImplementedError