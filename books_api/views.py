from django.shortcuts import render
from django.views.generic import ListView

from books_api.models import Books
# Create your views here.

class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'