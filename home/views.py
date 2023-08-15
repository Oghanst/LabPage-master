from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

# TODO: search all members in models to get all people
def people(request):
    return render(request, 'people.html')

def research(request):
    return render(request, 'research.html')

def news_events(request):
    return render(request, 'news_events.html')

def about(request):
    return render(request, 'about.html')
