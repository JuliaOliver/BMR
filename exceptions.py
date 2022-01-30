class BaseError(Exception):
    pass


class InvalidUsernameOrPasswordException(BaseError):
    def __init__(self):
        self.message = "Invalid Username or Password! Please try again!"

    def __str__(self):
        return self.message
