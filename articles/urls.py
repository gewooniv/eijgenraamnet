from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.MainPageView.as_view(), name='main-page'),
    path('posts', views.PostsView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.PostView.as_view(), name='post-page'),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]