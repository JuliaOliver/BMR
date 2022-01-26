class PublicationPost:
    def __init__(self, id_num=None, post_type=None, name=None, author_director=None, genre=None, post_content=None):
        self.id_num = id_num
        self.post_type = post_type
        self.name = name
        self.author_director = author_director
        self.genre = genre
        self.post_content = post_content

    def __str__(self):
        return f"| {self.id_num:20.20s} | {self.post_type:5.5s} " \
               f"| {self.name:15.15} | {self.author_director:20.20}" \
               f"| {self.genre:20.20} |\n| {self.post_content:91.91} |\n"
