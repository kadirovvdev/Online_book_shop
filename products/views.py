# from msilib.schema import ListView
from django.shortcuts import render
from django.views import View
from .models import Books, BookCategory
from django.shortcuts import render, get_object_or_404



# Create your views here.



class BookListView(View):
    def get(self, request):
        books = Books.objects.all().order_by('-id')
        return render(request, 'book/book_list.html', {'books': books})

# views.py

 # Assuming your Book model is in a file named models.py

def book_detail(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


# class BookListView(ListView):
#     model = Books
#     template_name = 'book/book_list.html'
#     context_object_name = 'book'
