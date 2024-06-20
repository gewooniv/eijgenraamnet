from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Comment, CustomUser



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ['username', 'text']
        exclude = ['post', 'date']
        labels = {
            'username': 'Naam',
            'text': 'Reactie'
        }
        error_messages = {
            'username': {
                'required': 'Je naam moet ingevuld worden, voor het verzenden van de reactie.',
                'max_length': 'De lengte van de naam is te groot.'
            },
            'text': {
                'required': 'Je bent de tekst vergeten.',
                'max_length': 'De lengte van de reactie is te groot.'
            }
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
                'cols': 40
            })
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name", 
            "last_name", 
            "email",
            "password", 
            "date_of_birth",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions"
        ]
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name", 
            "last_name", 
            "email", 
            "password",
            "date_of_birth",
            "is_staff",
            "is_active", 
            "groups",
            "user_permissions"
         ]