from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.


def home(request):
    return render(request, 'store_book.html')

def store_book(request):
    if request.method == "POST":
        book = BookStoreForm(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
            book.save(commit=True)
            return redirect("showbooks")
            
    else:
        book = BookStoreForm()
    return render(request, 'store_book.html', {'form': book})

def show_books(request):
    book = BookStoreModel.objects.all()
    return render(request, 'show_book.html', {'data': book})
