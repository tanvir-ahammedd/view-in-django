from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView
# Create your views here.

#functin based view
# def home(request):
#     return render(request, 'home.html')

# class based view
class MyTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roll = self.kwargs.get('roll', None)
        context = {   
            'name': 'Rahim',
            'age': 21,
            'roll': roll
        }
        context.update(kwargs)
        print(context)
        return context

def store_book(request):
    if request.method == "POST":
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save(commit=True)
            return redirect("showbooks")
    else:
        book = BookStoreForm()
    return render(request, 'store_book.html', {'form': book})

# def show_books(request):
#     book = BookStoreModel.objects.all()
#     return render(request, 'show_book.html', {'data': book})

#class based view
class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'data'
    
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(author='Rahim')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'data': BookStoreModel.objects.all().order_by('author')}
        return context
    
    # def get_context_data(self, **kwargs): #give same name to all category
    #     context = super().get_context_data(**kwargs)
    #     books = BookStoreModel.objects.all().order_by('author')
    #     for book in books:
    #         book.category = "Mango"
    #     context['data'] = books
    #     return context
    
    ordering = ['category']

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
