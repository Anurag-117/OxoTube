# serverapi\urls.py
from django.urls import path
from .views import *

app_name = "serverapi"
urlpatterns = [
    path('get_data', get_data, name='api'),
    path('dashboard_data/', DasboardData.as_view(), name='api-data'),
]