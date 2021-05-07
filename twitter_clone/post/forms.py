from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    text = forms.CharField(label='text')


