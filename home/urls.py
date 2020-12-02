# home\urls.py
from django.urls import path, re_path
from .views import *

app_name = "home"
urlpatterns = [
    path('', home_view, name='videosPage'),
]