from django.shortcuts import render


def home(request):
    """Home page for Learning Log app"""
    return render(request, 'learning_logs/home.html')
