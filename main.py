from dao_patterns.user_roles import UserRoles
from dao_patterns.posts_manager import PostsManager
from entities.publication_post import PublicationPost
from entities.users import User

if __name__ == '__main__':
    regular_user = User(None, "RegUs", "pass123")
    regular_user_2 = User(None, "RegUs2", "2pass123")
    admin_user = User(None, "AdmUs", "123pass")
    admin_user_2 = User(None, "AdmUs2", "123pass2")
    post_movie = PublicationPost(None, "movie", "First Movie", "First Director", "Boring, Anything",
                                 "This is the first movie to be reviewed")
    post_movie_2 = PublicationPost(None, "movie", "Lorem Ipsum", "Dolor Sit", "Comedy, Family",
                                   "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                                   "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    post_movie_3 = PublicationPost(None, "movie", "Blah Blah", "Random Name", "Horror, Thriller",
                                   "Ut enim ad minim veniam, quis nostrud exercitation ullamco "
                                   "laboris nisi ut aliquip ex ea commodo consequat")
    post_book = PublicationPost(None, "book", "First Book", "First Author", "First, Genre",
                                "This is the first book to be reviewed")
    post_book_2 = PublicationPost(None, "book", "Meh meh blah", "Random Author", "Fantasy, SiFi",
                                  "Duis aute irure dolor in reprehenderit in voluptate velit esse "
                                  "cillum dolore eu fugiat nulla pariatur")
    post_book_3 = PublicationPost(None, "book", "Grr Mrr", "Some Guy", "Some, Genre",
                                  "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui "
                                  "officia deserunt mollit anim id est laborum.")

    movies = (post_movie, post_movie_2, post_movie_3)
    books = (post_book, post_book_2, post_book_3)
    regulars = (regular_user, regular_user_2)
    admins = (admin_user, admin_user_2)

    roles = UserRoles()
    posts = PostsManager()

    for m in movies:
        posts.add_movie_post(m)
    for b in books:
        posts.add_book_post(b)
    for r in regulars:
        roles.add_regular_user(r)
    for a in admins:
        roles.add_admin_user(a)

    print("~~~~~~~~~~ Movie Posts ~~~~~~~~~~~")
    for el in posts.find_all_book_posts():
        print(el)
    print("~~~~~~~~~~ Movies Count ~~~~~~~~~~")
    print(posts.count_movie_posts())
    print("~~~~~~~~~~ Book Posts ~~~~~~~~~~~")
    for el in posts.find_all_movie_posts():
        print(el)
    print("~~~~~~~~~~ Books Count ~~~~~~~~~~")
    print(posts.count_book_posts())
    print("~~~~~~~~~~ Regular Users ~~~~~~~~~~~")
    for el in roles.find_all_regular_users():
        print(el)
    print("~~~~~~~~~~ Regular Users Count ~~~~~~~~~~")
    print(roles.regulars_count())
    print("~~~~~~~~~~ Admin Users ~~~~~~~~~~~")
    for el in roles.find_all_admin_users():
        print(el)
    print("~~~~~~~~~~ Admin Users Count ~~~~~~~~~~")
    print(roles.admins_count())
    print("~~~~~~~~~~ Remove Movie ~~~~~~~~~~~")
    posts.delete_by_id(post_movie.id_num)
    print("~~~~~~~~~~ Movie Posts ~~~~~~~~~~~")
    for el in posts.find_all_movie_posts():
        print(el)
    print("~~~~~~~~~~ Movies Count ~~~~~~~~~~")
    print(posts.count_movie_posts())
    print("~~~~~~~~~~ Remove Book ~~~~~~~~~~~")
    posts.delete_by_id(post_book_2.id_num)
    print("~~~~~~~~~~ Book Posts ~~~~~~~~~~~")
    for el in posts.find_all_book_posts():
        print(el)
    print("~~~~~~~~~~ Books Count ~~~~~~~~~~")
    print(posts.count_book_posts())
    print("~~~~~~~~~~ Change Regular User to Admin User ~~~~~~~~~")
    roles.regular_to_admin_user(regular_user_2)
    print("~~~~~~~~~~ Regular Users ~~~~~~~~~~~")
    for el in roles.find_all_regular_users():
        print(el)
    print("~~~~~~~~~~ Regular Users Count ~~~~~~~~~~")
    print(roles.regulars_count())
    print("~~~~~~~~~~ Admin Users ~~~~~~~~~~~")
    for el in roles.find_all_admin_users():
        print(el)
    print("~~~~~~~~~~ Admin Users Count ~~~~~~~~~~")
    print(roles.admins_count())
