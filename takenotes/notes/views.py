from django.shortcuts import render, get_object_or_404
from .models import Note
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    #Make a login portal
    user=User.objects.get(username="evilcraft68")
    return render(request,'notes/login.html',{})

def notelist(request):
    user=User.objects.get(username="evilcraft68")
    notelist1=Note.objects.filter(author=user)
    return render(request,'notes/noteslist.html',{'notelist': notelist1})

def viewnote(request,pk):
    note=get_object_or_404(Note, pk=pk)
    return render(request, 'notes/viewnote.html',{'note':note})

def newnote(request):
    return