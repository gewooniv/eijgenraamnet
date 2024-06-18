from django.urls import path
from . import views

urlpatterns = [
    path('guestbook', views.GuestbookView.as_view(), name='guestbook'),
    path('guestbook/response', views.add_response, name='response')
]
