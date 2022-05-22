"""Defining URL-patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('topics/', views.topics, name='topics'),  # Page with topics list
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # Page with detailed information for current topic
    path('new_topic/', views.new_topic, name='new_topic'),  # Page for adding new topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),  # Page for adding new entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # Page for entry editing
]
