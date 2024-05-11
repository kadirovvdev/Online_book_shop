from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('test/', BookListView.as_view(), name='list')

]