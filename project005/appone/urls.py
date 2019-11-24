# pages/urls.py
from django.urls import path
from .views import IndexView,HomePageView, SelectView, PostView, PostDetailView
urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('select/', SelectView, name='select'),
   path('post/new/', PostView.as_view(), name='post_new'), # new
   path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   path('home/<int:key>/', HomePageView, name='home')
]
