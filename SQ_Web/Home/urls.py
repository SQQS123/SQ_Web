from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
 path('', views.home, name='home'),
 # register
 path('register/', views.register, name = 'register'),
 path("register_success/", views.user_register_success, name='register_success'),
 path("register_fail/", views.user_register_fail, name="register_fail"),
 path('login/', views.login, name='login'),
]