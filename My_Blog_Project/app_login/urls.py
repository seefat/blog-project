from django.urls import path,re_path 
from . import views
app_name = 'app_login'

urlpatterns = [
    path('signup/',views.signup, name = 'signup'),
    path('login/',views.login_page, name = 'login'),
    path('logout/', views.logout_user, name = 'logout')
]
