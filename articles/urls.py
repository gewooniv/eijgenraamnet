from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('posts/', views.posts, name='posts'),
    path('posts/<slug:slug>', views.post_page, name='post_page'),
]