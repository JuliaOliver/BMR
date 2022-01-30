class User:
    def __init__(self, id_num=None, username=None, first_name=None,
                 last_name=None, email=None, password=None):
        self.id_num = id_num
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        return f"| {self.id_num:20.20} | {self.username:10.10} |\n"
