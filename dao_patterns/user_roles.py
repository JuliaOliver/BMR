from dao_patterns.main_repository import MainRepo


class UserRoles(MainRepo):
    def __init__(self):
        super().__init__()
        self.regular_users = {}
        self.admin_users = {}

    def add_regular_user(self, user):
        self.add_entity(user)
        self.regular_users[user.id_num] = user
        return user

    def add_admin_user(self, user):
        self.add_entity(user)
        self.admin_users[user.id_num] = user
        return user

    def regular_to_admin_user(self, user):
        user_id = user.id_num
        self.regular_users.pop(user_id)
        self.admin_users[user_id] = user

    def find_all_regular_users(self):
        return self.regular_users.values()

    def find_all_admin_users(self):
        return self.admin_users.values()

    def find_admin_by_id(self, id_num):
        if id_num not in self.admin_users:
            return None
        return self.admin_users[id_num]

    def find_regular_by_id(self, id_num):
        if id_num not in self.regular_users:
            return None
        return self.regular_users[id_num]

    def admins_count(self):
        return len(self.admin_users)

    def regulars_count(self):
        return len(self.regular_users)

    def remove_user(self, user):
        if user.id_num in self.regular_users:
            self.regular_users.pop(user.id_num)
        elif user.id_num in self.admin_users:
            self.admin_users.pop(user.id_num)
        self.delete_entity(user)
