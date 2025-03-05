"""
URL configuration for pizza_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    """
    Simple home route to provide API information
    """
    return JsonResponse({
        "message": "Pizza Ordering API",
        "available_endpoints": [
            {
                "path": "/menu",
                "method": "GET",
                "description": "Fetch all pizzas or a specific pizza by name",
                "example": "/menu?name=Margherita"
            },
            {
                "path": "/order",
                "method": "POST",
                "description": "Place an order for pizzas",
                "example_body": "[{\"id\": 1, \"quantity\": 2}]"
            }
        ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add a root path handler
    path('menu', include('pizza_api.urls')),  # Ensure this matches your views
    path('order', include('pizza_api.urls')),
]