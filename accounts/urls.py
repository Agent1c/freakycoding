from django import views
from django.urls import path
from . views import Home, LoginView, RegisterView


urlpatterns = [
    path('', Home, name="home" ),
    path('login/', LoginView, name='login'),
    path('register/',RegisterView, name="register"),
]
