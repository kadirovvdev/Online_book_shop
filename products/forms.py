from django.forms import ModelForm
from .models import Books
from django import forms



from products.models import Review


class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']



class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'price', 'page', 'image', 'category', 'book_lang']


