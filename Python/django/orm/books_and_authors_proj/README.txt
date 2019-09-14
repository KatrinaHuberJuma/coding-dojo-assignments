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
