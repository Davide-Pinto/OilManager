from django.urls import path
from . import views  # Import the views module from your app

urlpatterns = [
    path('', views.home, name='home'),  # Set the root URL to use the home view
    # ... other url patterns ...
]