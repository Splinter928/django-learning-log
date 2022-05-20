from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm


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


def new_topic(request):
    """Defining new topic"""
    if request.method != 'POST':  # data not send, empty form creation
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)  # POST data sent, data processing
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # output an empty or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Defining new entry"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # output an empty or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
