from django.urls import path
from . import views

app_name = "Personal"
urlpatterns = [
    path('', views.personal, name="personal"),
]