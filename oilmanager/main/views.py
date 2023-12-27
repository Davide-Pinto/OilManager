from django.shortcuts import render
from .models import Cliente
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def clients(request):
    data = Cliente.objects.all()
    paginator = Paginator(data, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'pagr_obj': page_obj,
    }
    return render(request, 'client_list.html', context)

def lagares(request):
    return render(request, 'lagares.html')

def loads(request):
    return render(request, 'loads.html')

def stats(request):
    return render(request, 'stats.html')

def dashboard(request):
    return render(request, 'dashboard.html')