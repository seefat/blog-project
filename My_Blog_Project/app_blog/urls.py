from django.urls import path, re_path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list')
]
