from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.Customerlist, name='customer-list')
]
