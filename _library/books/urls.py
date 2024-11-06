from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('treeTables', views.tree_tables),
    path('addBook', views.add_book),
    path('addAuthor', views.add_author),
    path('deleteBook/<int:id>', views.delete_book),
    path('deleteAuthor/<int:id>', views.delete_author),
]