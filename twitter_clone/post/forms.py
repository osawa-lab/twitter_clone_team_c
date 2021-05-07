from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'text',
        )
        widgets = {
            'text': forms.Textarea(
                attrs={'rows': 10, 'cols': 30, 'placeholder': 'ここに入力'}
            ),
        }
