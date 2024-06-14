from django.shortcuts import render
from django.views import View
from .models import Picture

# Create your views here.

def index(request):
    pictures = Picture.objects.all()
    context = {
        'pictures': pictures
    }
    return render(request, 'gallery/index.html', context)