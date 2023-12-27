from django.shortcuts import render
from .models import Cliente
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def clients(request):
    search_query = request.GET.get("search-bar", "")
    if search_query:
        # Initialize an empty QuerySet
        data = Cliente.objects.none()

        # Check if search_query can be converted to an integer for ID search
        try:
            client_id = int(search_query)
            data |= Cliente.objects.filter(id=client_id)
        except ValueError:
            pass  # search_query wasn't an integer, so we skip ID search
        
        # Continue with other fields
        data |= Cliente.objects.filter(
            Q(nome__icontains=search_query) |
            Q(morada__icontains=search_query) |
            Q(contacto=search_query)
        )
    else:
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