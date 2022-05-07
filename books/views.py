from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'books/home.html')

def about(request):
    return render(request, 'books/about.html')