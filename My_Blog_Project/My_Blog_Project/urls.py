
from django.contrib import admin
from django.urls import path
#from app_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', views.app_login, name = 'login'),
    path('blog/', views.app_blog,name='blog'), 
]
