from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Books, Review
from .forms import BookForm, AddReviewForm

class BookListView(View):
    def get(self, request):
        books = Books.objects.all().order_by('-id')
        return render(request, 'book/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        reviews = Review.objects.filter(book=pk)
        context = {
            'book': book,
            'reviews': reviews
        }
        return render(request, 'book_detail.html', context=context)

class BookCreateView(View):
    template_name = 'book/book_create.html'

    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:book-list')
        return render(request, self.template_name, {'form': form})

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('products:book-list')

class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'book': book,
            'add_review_form': add_review_form
        }
        return render(request, 'book/add_review.html', context=context)

    def post(self, request, pk):
        book = Books.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                book=book,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('products:book-detail', pk=pk)

class BookUpdateView(View):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        form = BookForm(instance=book)
        return render(request, 'update.html', {'form': form, 'book': book})

    def post(self, request, pk):
        book = Books.objects.get(pk=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('products:book-detail', pk=pk)
        return render(request, 'update.html', {'form': form, 'book': book})

class ReviewUpdate(View):
    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        form = AddReviewForm(instance=review)
        if review.user != request.user:
            return HttpResponseForbidden("You cannot edit another user's review!")
        return render(request, 'review_update.html', {'form': form, 'review': review})

    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        form = AddReviewForm(request.POST, instance=review)
        if review.user != request.user:
            return HttpResponseForbidden("You cannot edit another user's review!")
        if form.is_valid():
            form.save()
            return redirect('products:book-detail', pk=review.book.pk)
        return render(request, 'review_update.html', {'form': form, 'review': review})

class ReviewDelete(View):
    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        if review.user != request.user:
            return HttpResponseForbidden("You cannot delete another user's review!")
        return render(request, 'review_confirm_delete.html', {'review': review})

    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        if review.user != request.user:
            return HttpResponseForbidden("You cannot delete another user's review!")
        review.delete()
        return redirect('products:book-detail', pk=review.book.pk)
