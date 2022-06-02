from django.forms import PasswordInput
from django.shortcuts import render, get_object_or_404, redirect

from notes.forms import NoteForm, LoginForm
from .models import Note, User
# Create your views here.
global isloggedin
user=0

def login(request):
    if request.method=="POST":
        form= LoginForm(request.POST)
        if form.is_valid():
            try:
                myuser=User.objects.get(email=request.POST['email'],password=request.POST['password'])
                global user
                user=get_object_or_404(User,pk=myuser.pk)
                return redirect('noteshomeroute')
            except User.DoesNotExist:
                return render(request,'notes/login.html',{'form': form,'error': 'Invalid Credentials'})
    else:
        form= LoginForm()
    return render(request,'notes/login.html',{'form': form,'error': ''})

def notelist(request):
    notelist1=Note.objects.filter(author=user)
    return render(request,'notes/noteslist.html',{'notelist': notelist1})

def viewnote(request,pk):
    note=get_object_or_404(Note, pk=pk)
    return render(request, 'notes/viewnote.html',{'note':note})

def newnote(request):
    if request.method=="POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.savetoapp()
            return redirect('singlenote',pk=post.pk)
    else:
        form = NoteForm()
    return render(request,'notes/editnote.html',{'form': form})

def changenote(request,pk):
    post = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.savetoapp()
            return redirect('singlenote', pk=post.pk)
    else:
        form = NoteForm(instance=post)
    return render(request, 'notes/editnote.html', {'form': form})