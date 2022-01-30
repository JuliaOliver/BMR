from entities.users import User


class AdminUser(User):
    def __init__(self):
        super().__init__()

    def add_movie_post(self):
        pass

    def add_book_post(self):
        pass

    def change_user_permissions(self):
        pass

    def remove_user(self):
        pass
