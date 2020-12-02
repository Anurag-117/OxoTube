# analytics\urls.py
from django.urls import path
from .views import *

app_name = "analytics"
urlpatterns = [
    path('', dashboard_view, name='dashboardPage'),
]