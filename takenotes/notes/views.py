from django.shortcuts import render
from .models import Note
# Create your views here.

def login(request):
    return render(request,'notes/login.html',{})