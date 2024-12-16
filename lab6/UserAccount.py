class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def get_info(self):
        return self.username, self.email, self.password
    def set_password(self, new_password):
        self.password = new_password
    def check_password(self, password_check):
        if self.password == password_check:
            return True
        else:
            return False
Anton = UserAccount('Anton','Anton2929@gmail.com',123)
print(Anton.check_password(123))
print(Anton.set_password(1234))
print(Anton.check_password(123))
print(Anton.get_info())
