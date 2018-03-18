from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
# Create your views here.
def index(request):
    data = {
        "books": Books.objects.all()
    }
    return render(template_name="books/index.html", request=request, context=data)

def listBooks(request):
    return HttpResponse("Aquí deberían estar los libros")