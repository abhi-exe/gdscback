from dataclasses import fields
from django import forms
from .models import Note, User

class NoteForm(forms.ModelForm):
    class Meta:
        model= Note
        fields = ('title','text','tags')

class LoginForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=('email','password')