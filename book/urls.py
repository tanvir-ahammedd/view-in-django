from django.urls import path

from . import views

urlpatterns = [
    # path('', views.TemplateView.as_view(template_name='home.html'), name="homepage"), #template view
    path('', views.MyTemplateView.as_view(template_name='home.html'), name='homepage'),
    path('<int:roll>/', views.MyTemplateView.as_view(template_name='home.html'),name='homepage_with_roll'),
    path('store_new_book/', views.store_book, name="bookstore"),
    # path('show_book/', views.show_books, name="showbooks"),
    path('show_book/', views.BookListView.as_view(), name="showbooks"),
    path('book_details/<int:id>', views.BookDetailsView.as_view(), name="book_details"),
    path('delete_book/<int:id>', views.delete, name="deletebooks"),
    path('edit_book/<int:id>', views.edit, name="editbook")
]
