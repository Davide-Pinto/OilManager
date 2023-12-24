from django.urls import path
from . import views  # Import the views module from your app

urlpatterns = [
    path('', views.home, name='home'),  # Set the root URL to use the home view
    path('clients/', views.clients, name='clients'),
    path('lagares/', views.lagares, name='lagares'),
    path('loads/', views.loads, name='loads'),
    path('stats/', views.stats, name='stats'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    # ... other url patterns ...
]