from users import User


class LoginController:
    def __init__(self):
        self.user = User()

    def register(self):
        self.user.username = input("Enter Username: ")
        self.user.email = input("Enter Email: ")
        self.user.first_name = input("Enter your first name: ")
        self.user.last_name = input("Enter your last name: ")
        self.user.password = input("Enter Password: ")

    def log_in(self):
        pass

    def log_out(self):
        pass

    def get_logged_user(self):
        pass
