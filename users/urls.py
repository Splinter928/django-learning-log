"""Defining URL-patterns for users"""
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Turn ON default URL-authorization
    path('', include('django.contrib.auth.urls'))
]
