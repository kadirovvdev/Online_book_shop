from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('tests/', BookListView.as_view(), name='list')

]