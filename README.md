# Project name: 
Books and Movies Reviews (BMR)

# Project description: 
Nowadays movies and TV series are much more accessible,
and books are having a new wave of interest. But all of this causes tons of new 
movies and books on the market and sometimes makes it hard to find out which one 
is for you and which not. BMR gives the chance to rate movies and books and to write 
them reviews, so the other users can judge whether it is for them or not.

# The main user roles (actors in BMR) are:
• Anonymous/Guest user - can only view the rates and the reviews for the 
movies and the books, without rating and writing ones. This user does not need to register <p>
• Registered user - can view the rates and the reviews, but also can give and write ones <p>
• Administrator - can manage the Registered users and the content. 
Adds the movies and the books to the page, edits them. Can delete registered user <p>

Users with administrator roles would be able to create and upload the content
of the project (posts about books and movies). They will have rights to manage other
users and all the posts. They could delete comments (reviews) under the posts, if needed.
Also administrator users will be the one who will be able to create and upload
different rankings (e.g. Top Ten books/movies...)

Regular users will only be able to add comments (reviews) and give
rates.

There would be an option to convert Regular user to Administrator.

# Current implementation:
The current implementation consist of two modules `dao_patterns` and
`entities`. There are separated the main Singleton classes for both
the posts and the users allowing to find (read), create, update, and 
delete (CRUD) entities of that particular type, keeping the created
entity instances in memory, in a dictionaries.

In the `main.py` file there are instantiated all the classes and
executed almost all of the CRUD methods and printed the results
of every method, separated with brief descriptive print.
