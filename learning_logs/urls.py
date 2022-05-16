"""Defining URL-patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('topics/', views.topics, name='topics'),  # Page with topics list
    path('topics/<int:topic_id>/', views.topic, name='topic')  # Page with detailed information for current topic
]
