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
            book.save(commit=True)
            return redirect("showbooks")
            
    else:
        book = BookStoreForm()
    return render(request, 'store_book.html', {'form': book})

def show_books(request):
    book = BookStoreModel.objects.all()
    return render(request, 'show_book.html', {'data': book})

def delete(request, id):
    std = BookStoreModel.objects.get(pk=id).delete()
    return redirect("showbooks")

def edit(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method=='POST': 
        form = BookStoreForm(request.POST, instance=book)  
        if form.is_valid():
            form.save(commit=True)
            return redirect("showbooks")
    return render(request, 'store_book.html', {'form': form})
