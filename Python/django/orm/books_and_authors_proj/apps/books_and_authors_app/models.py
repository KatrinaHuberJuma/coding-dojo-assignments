from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __repr__(self):
        return f"<Book object: {self.title}, description: {self.description}>"
        

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.CharField(max_length=255, default="no notes")
    def __repr__(self):
        return f"<Author object: {self.first_name} {self.last_name}>"