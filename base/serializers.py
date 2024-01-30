from rest_framework import serializers
from .models import Customer, Business, Business_Category, Location

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_Category
        fields = "__all__"

class  LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['county', 'sub_county', 'ward', 'building_name', 'floor']

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"