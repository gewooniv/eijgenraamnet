from django.urls import path
from . import views

urlpatterns = [
    path('guestbook', views.GuestbookView.as_view(), name='guestbook')
]
