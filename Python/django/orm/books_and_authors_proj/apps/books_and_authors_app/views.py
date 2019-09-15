from django.shortcuts import render, redirect
from .models import Book, Author


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     def __repr__(self):
#         return f"<Book object: {self.title}, description: {self.description}>"
        

# class Author(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     books = models.ManyToManyField(Book, related_name="authors")
#     notes = models.CharField(max_length=255, default="no notes")
#     def __repr__(self):
#         return f"<Author object: {self.first_name} {self.last_name}>"

def books_page(request):
    context = {
        "books": Book.objects.all(),
    }
    return render(request, "books_and_authors_app/books.html", context)


def add_book(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        title = request.POST["book_title"]
        description = request.POST["book_description"]
        Book.objects.create(title=title, description=description)
        return redirect("/")

def add_author_to_book(request, book_id):
    print(request)
    if request.method == "GET":
        return redirect("/books/" + str(book_id))
    if request.method == "POST":
        author_id = request.POST["author_id"]
        Book.objects.get(id=book_id).authors.add(Author.objects.get(id=author_id))
        return redirect("/")


def authors_page(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request, "books_and_authors_app/authors.html", context)

def one_book(request, book_id):
    book = Book.objects.get(id=book_id)
    this_book_authors = book.authors.all()
    all_authors = Author.objects.all()
    other_authors = [author for author in all_authors if author not in this_book_authors]
    context ={
        "book": book,
        "other_authors": other_authors,
    }
    
    return render(request, "books_and_authors_app/book.html", context)