from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,related_name="books",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_author(name):
    Author.objects.create(name = name)

def create_book(title , author_id):
    Book.objects.create(title = title , author = Author.objects.get(id = author_id) )

def get_all_authors():
    return Author.objects.all()

def get_all_books():
    return Book.objects.all()

def delete_author(id):
    c = Author.objects.get(id = id)
    c.delete()

def delete_book(id):
    c = Book.objects.get(id = id)
    c.delete()
