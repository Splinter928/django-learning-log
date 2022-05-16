from django.shortcuts import render
from .models import Topic


def home(request):
    """Home page for Learning Log app"""
    return render(request, 'learning_logs/home.html')


def topics(request):
    """Displays topics list"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Displays one topic and all its records"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  # '-' for reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
