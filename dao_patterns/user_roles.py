import uuid


class UserRoles:
    def __init__(self):
        self.regular_users = {}
        self.admin_users = {}

    def add_regular_user(self, user):
        user.id_num = str(uuid.uuid1())
        self.regular_users[user.id_num] = user
        return user

    def add_admin_user(self, user):
        user.id_num = str(uuid.uuid1())
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
