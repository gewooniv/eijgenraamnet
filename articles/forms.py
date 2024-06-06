from django import forms
from .models import CommentForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        # fields = ['username', 'text']
        exclude = ['post', 'date']
