# from msilib.schema import ListView
from django.shortcuts import render
from django.views import View
from .models import Books, BookCategory


# Create your views here.



class BookListView(View):
    def get(self, request):
        books = Books.objects.all().order_by('-id')
        return render(request, 'book/book_list.html')

# class BookListView(ListView):
#     model = Books
#     template_name = 'book/book_list.html'
#     context_object_name = 'book'
