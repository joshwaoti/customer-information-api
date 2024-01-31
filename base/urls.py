from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer-list'),
    path('customer-detail/<int:pk>/', views.customer_detail, name='customer-details'),
    path('businesses/', views.business_list, name='business-list'),
    path('business-detail/<int:pk>/', views.business_details, name='business-details'),
]
