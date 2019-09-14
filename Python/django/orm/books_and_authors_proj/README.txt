from apps.books_and_authors_app.models import Book, Author

c_sharp = Book.objects.create(title="C Sharp", description="about C Sharp")
java = Book.objects.create(title="Java", description="about Java")
python = Book.objects.create(title="Python", description="about Python")
php = Book.objects.create(title="PHP", description="about PHP")
ruby = Book.objects.create(title="Ruby", description="about Ruby")




Jane Austen, Emily Dickinson, Fyodor Dostoevksy, William Shakespeare, Lau Tzu

jane_a = Author.objects.create(first_name="Jane", last_name="Austen")
emily_d = Author.objects.create(first_name= "Emily", last_name="Dickinson")
fydor_d = Author.objects.create(first_name= "Fyodor", last_name= "Dostoevksy")
will_s = Author.objects.create(first_name= "William", last_name= "Shakespeare")
lau_t = Author.objects.create(first_name= "Lau", last_name= "Tzu")


>>> c_sharp = Book.objects.get(title="C Sharp")
>>> c_sharp
<Book object: C Sharp, description: about C Sharp>
>>> c_sharp.title="C#"

bill = Author.objects.get(id=4)


first_author.books.add(Book.objects.first())
>>> first_author.books.add(Book.objects.get(id=4))
>>> first_author.books.all()

books_in_order = Book.objects.all().order_by("id")
for i in range(2):
...     books_in_order[i].authors.add(Author.objects.get(id=2))

Author.objects.get(id=2).books.all()
<QuerySet [<Book object: Java, description: about Java>, <Book object: Python, description: about Python>]

for i in range(3):
...     books_in_order[i].authors.add(Author.objects.get(id=3))

>>> for i in range(3):
...     books_in_order[i].authors.add(Author.objects.get(id=3))
... 
>>> Author.objects.get(id=3).books.all()
<QuerySet [<Book object: Java, description: about Java>, <Book object: Python, description: about Python>, <Book object: PHP, description: about PHP>]>


test_dude = Author.objects.create(first_name= "test", last_name= "Tzu")
>>> test_dude.books.add(Book.objects.get(id=1), Book.objects.get(id=2), Book.objects.get(id=3),Book.objects.get(id=4),Book.objects.get(id=5))
>>> test_dude.books.all()
<QuerySet [<Book object: Java, description: about Java>, <Book object: Python, description: about Python>, <Book object: PHP, description: about PHP>, <Book object: Ruby, description: about Ruby>, <Book object: C Sharp, description: about C Sharp>]>

>>> Book.objects.get(id=3).authors.all()
<QuerySet [<Author object: Fyodor Dostoevksy>, <Author object: test Tzu>]>
>>> 

>>> Author.objects.get(id=4).books.add(Book.objects.all())

>>> third_book = Book.objects.get(id=3)
>>> third_book_first_auth = third_book.authors.first()
>>> third_book.authors.all()
<QuerySet [<Author object: Fyodor Dostoevksy>, <Author object: test Tzu>, <Author object: William Shakespeare>]>
>>> third_book.authors.remove(third_book_first_auth)
>>> third_book.authors.all()
<QuerySet [<Author object: test Tzu>, <Author object: William Shakespeare>]>
>>> 


>>> Book.objects.get(id=2).authors.add(Author.objects.get(id=5))
>>> Book.objects.get(id=2).authors.all()
<QuerySet [<Author object: Emily Dickinson>, <Author object: Fyodor Dostoevksy>, <Author object: test Tzu>, <Author object: William Shakespeare>, <Author object: Lau Tzu>]>

>>> books_of_third_auth = Author.objects.get(id=3).books.all()
>>> books_of_third_auth
<QuerySet [<Book object: Java, description: about Java>, <Book object: Python, description: about Python>]>


>>> authors_of_book_5 = Book.objects.get(id=5).authors.all()
>>> authors_of_book_5
<QuerySet [<Author object: test Tzu>, <Author object: William Shakespeare>]>
>>> 

