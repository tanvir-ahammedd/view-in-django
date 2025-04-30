from django.urls import path

from book.views import home, store_book, show_books

urlpatterns = [
    path('', home),
    path('store_new_book/', store_book, name="bookstore"),
    path('show_book/', show_books, name="showbooks")
]
