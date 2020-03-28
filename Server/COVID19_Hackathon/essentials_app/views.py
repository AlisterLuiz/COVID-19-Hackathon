from django.shortcuts import render

# Create your views here.

def hi(request):
    return render(request, 'essentials_app/hi.html')