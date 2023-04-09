from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'my_hobby.html')

def about(request):
    return render(request, 'about_me.html')

def my_contacts(request):
    return render(request, 'my_contacts.html')
