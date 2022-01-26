class User:
    def __init__(self, id_num=None, username=None, password=None):
        self.id_num = id_num
        self.username = username
        self.password = password

    def __str__(self):
        return f"| {self.id_num:20.20} | {self.username:10.10} |\n"
