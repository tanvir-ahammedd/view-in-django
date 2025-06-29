from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
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

# def store_book(request):
#     if request.method == "POST":
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save(commit=True)
#             return redirect("showbooks")
#     else:
#         book = BookStoreForm()
#     return render(request, 'store_book.html', {'form': book})

# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     # success_url = "/show_book/"
#     # success_url = reverse_lazy('showbooks')
#     def form_valid(self, form):
#         # return HttpResponse("Form Submitted")
#         form.save()
#         return redirect("showbooks")

class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy("showbooks")
    

# def show_books(request):
#     book = BookStoreModel.objects.all()
#     return render(request, 'show_book.html', {'data': book})

#List view of class based view
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

class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy("showbooks")
    
class BookDeleteView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy("showbooks")
    
# def delete(request, id):
#     std = BookStoreModel.objects.get(pk=id).delete()
#     return redirect("showbooks")
 #class Based View
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'

def edit(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method=='POST': 
        form = BookStoreForm(request.POST, instance=book)  
        if form.is_valid():
            form.save(commit=True)
            return redirect("showbooks")
    return render(request, 'store_book.html', {'form': form})
