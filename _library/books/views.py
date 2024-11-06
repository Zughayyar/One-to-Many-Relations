from django.shortcuts import render, redirect, HttpResponse
from . import models

def index(request):
    context = {
        'all_authors' : models.get_all_authors(),
        'all_books'   : models.get_all_books()
    }
    return render(request , "index.html" , context)

def tree_tables(request):
    context = {
        'all_authors' : models.get_all_authors()
    }
    return render(request , "treeTable.html" , context)

def add_book(request):
    if request.method == "POST":
        models.create_book(request.POST['book_title'] , request.POST['author_id'])
        return redirect('/')
    else:
        return HttpResponse("Ooops, Something went wrong")
    return redirect('/')

def add_author(request):
    if request.method == "POST":
        models.create_author(request.POST['author_name'])
        return redirect('/')
    else:
        return HttpResponse("Ooops, Something went wrong")

def delete_book(request, id):
    models.delete_book(id)
    return redirect('/')

def delete_author(request, id):
    models.delete_author(id)
    return redirect('/')