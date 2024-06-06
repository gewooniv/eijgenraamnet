from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('posts', views.PostsView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.PostView.as_view(), name='post_page'),
    path('thank-you', views.thank_you)
]