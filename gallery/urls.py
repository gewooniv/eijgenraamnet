from django.urls import include, path
from . import views



urlpatterns = [
    path('gallery', views.index, name='gallery'),
]