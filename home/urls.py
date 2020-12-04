# home\urls.py
from django.urls import path, re_path
from .views import *

app_name = "home"
urlpatterns = [
    path('', signup_view, name='signUpPage'),
    path('login/', signin_view, name='logInPage'),
    path('video/', home_view, name='videosPage'),
    path('logout/', logout_view, name='logOutPage')
]