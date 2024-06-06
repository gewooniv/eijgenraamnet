from django import forms
from .models import Comment

class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ['username', 'text']
        exclude = ['post', 'date']
