from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='books-home'),
    path('books/',views.books,name='books-books'),
    path('about/',views.about,name='books-about'),
]