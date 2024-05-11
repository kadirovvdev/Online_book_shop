from django.contrib import admin
from .models import Review, Books, Author, BookCategory, Language, Book_author


admin.site.register(Author)
admin.site.register(BookCategory)
admin.site.register(Language)
admin.site.register(Books)
admin.site.register(Book_author)
admin.site.register(Review)

# Register your models here.
