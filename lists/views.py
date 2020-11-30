from django.shortcuts import render, redirect
from . import models
from .forms import BookListForm

# Create your views here.
def list_books(request):
    if request.method == 'POST' :
        form = BookListForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/')
    
    bookList = models.BoookList.objects.all()
    form = BookListForm()
    context = {"bookList" : bookList, 'form' : form}
    return render(request, 'listBooks.html', context)


def delete_book(request, pk):
    item = models.BoookList.objects.get(id=pk)
    item.delete()
    return redirect('/')