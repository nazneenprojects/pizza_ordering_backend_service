
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_menu, name='menu'),  # Handle both /menu and /order
    path('', views.place_order, name='order'),
]