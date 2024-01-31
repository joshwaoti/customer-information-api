from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Customer, Business, Business_Category, Location
from .serializers import CustomerSerializer, BusinessCategorySerializer, BusinessSerializer, LocationSerializer

@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True,  context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def  customer_detail(request, pk):

    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "GET":
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)
        
    elif request.method == "PUT":
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST'])
def business_list(request):
    if request.method == "GET":
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True, context={'request': request})
        return Response(serializer.data)
    

    elif request.method == 'POST':
        # Extract location data from the request
        

        # Create or update the Business instance
        business_serializer = BusinessSerializer(data=request.data, context={'request': request})
        if business_serializer.is_valid():
            business_serializer.save()
            return Response(business_serializer.data, status=status.HTTP_201_CREATED)
        return Response(business_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def business_details(request, pk):
    business = get_object_or_404(Business, pk=pk)

    if request.method == "GET":
        serializer = BusinessSerializer(business, context={'request': request})
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BusinessSerializer(business, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)