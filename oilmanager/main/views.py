from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def clients(request):
    return render(request, 'client_list.html')

def lagares(request):
    return render(request, 'lagares.html')

def loads(request):
    return render(request, 'loads.html')

def stats(request):
    return render(request, 'stats.html')

def dashboard(request):
    return render(request, 'dashboard.html')