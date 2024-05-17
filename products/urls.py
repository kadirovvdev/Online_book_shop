from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='create-book'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/review/add/', views.AddReviewView.as_view(), name='add-review'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review-delete'),
]
