from django.urls import path
from . import views

app_name = "Comics"

urlpatterns = [
 path('', views.Comics, name='comics'),
 path('submit/', views.Submit_paint, name='submit'),
]