from django.shortcuts import render
from .models import Cliente
from django.core.paginator import Paginator
from django.db.models import Q
from main.forms import ClientForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'dashboard.html')

def clients(request):
    #Add Client to DB
    form = ClientForm(request.POST or None)
    if request.method =='POST':
        print("Form is invalid. SHIT:", form.errors)
        if 'submit' in request.POST:
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Ficha criada com Sucesso")
            else:
               print("Form is invalid. Errors:", form.errors)
    else:
        form = ClientForm()
        
    #-----------------END ADD-CLIENT-TO-DB-----------------------
    #----------------------SEARCH BAR----------------------------
    search_query = request.GET.get("search-bar", "")
    if search_query:
        # Initialize an empty QuerySet
        data = Cliente.objects.none().order_by('id')

        # Check if search_query can be converted to an integer for ID search
        try:
            client_id = int(search_query)
            data |= Cliente.objects.filter(id=client_id).order_by('id')
        except ValueError:
            pass  # search_query wasn't an integer, so we skip ID search
        
        # Continue with other fields
        data |= Cliente.objects.filter(
            Q(nome__icontains=search_query) |
            Q(morada__icontains=search_query) |
            Q(contacto=search_query)
        ).order_by('id')
    else:
        data = Cliente.objects.all().order_by('id')
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    #-----------------END-SEARCH-BAR-------------------------------
    
    context = {
        'pagr_obj': page_obj,
        'form':form,
        'search_query': search_query,
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