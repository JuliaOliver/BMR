import uuid


class PostsManager:
    def __init__(self):
        self.movie_posts = {}
        self.book_posts = {}

    def add_movie_post(self, post):
        post.id_num = str(uuid.uuid1())
        self.movie_posts[post.id_num] = post
        return post

    def add_book_post(self, post):
        post.id_num = str(uuid.uuid1())
        self.book_posts[post.id_num] = post
        return post

    def update(self, post):
        if post.post_type == "movie":
            if post.id_num not in self.movie_posts:
                return None
            self.movie_posts[post.id_num] = post

        elif post.post_type == "book":
            if post.id_num not in self.book_posts:
                return None
            self.book_posts[post.id_num] = post

        return post

    def delete_by_id(self, id_num):
        if id_num in self.movie_posts:
            old = self.movie_posts[id_num]
            self.movie_posts.pop(id_num)
            return old

        elif id_num in self.book_posts:
            old = self.book_posts[id_num]
            self.book_posts.pop(id_num)
            return old

        else:
            return None

    def find_all_movie_posts(self):
        return self.movie_posts.values()

    def find_all_book_posts(self):
        return self.book_posts.values()

    def find_by_id(self, id_num):
        if id_num in self.movie_posts:
            return self.movie_posts[id_num]
        elif id_num in self.book_posts:
            return self.book_posts[id_num]
        else:
            return None

    def count_movie_posts(self):
        return len(self.movie_posts)

    def count_book_posts(self):
        return len(self.book_posts)

    def count_all_posts(self):
        all_posts_count = len(self.movie_posts) + len(self.book_posts)
        return all_posts_count
