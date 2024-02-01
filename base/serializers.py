from rest_framework import serializers
from .models import Customer, Business, BusinessCategory, Location
from django.utils import timezone


class CustomerSerializer(serializers.ModelSerializer):

    customer_details_url = serializers.HyperlinkedIdentityField(
        view_name='customer-details',
        lookup_field='pk'
    )
    class Meta:
        model = Customer
        fields = ['id', 'name', 'customer_phone', 'customer_email', 'date_of_birth', 'nationality', 'customer_details_url']



class  LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['county', 'sub_county', 'ward', 'building_name', 'floor']

class BusinessSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    # calculated_age = serializers.CharField('calculated_age', read_only=True)
    location = LocationSerializer()

    business_details_url = serializers.HyperlinkedIdentityField(
        view_name='business-details',
        lookup_field='pk'
    )
    class Meta:
        model = Business
        fields = ['id', 'name', 'registration_date', 'calculated_age', 'category', 'category_name', 'customer', 'customer_name', 'location', 'business_details_url']

    def clean_registration_date(self, value):
        """
        Ensure that registration_date is not in the future.
        """
        if value > timezone.now().date():
            raise serializers.ValidationError("Registration date cannot be in the future.")
        return value
    
    def update(self, instance, validated_data):
        # Update standard fields
        instance.name = validated_data.get('name', instance.name)
        instance.registration_date = validated_data.get('registration_date', instance.registration_date)

        # Update nested fields (category, customer, location)
        instance.category = validated_data.get('category', instance.category)
        instance.customer = validated_data.get('customer', instance.customer)

        # Handle location update or creation
        location_data = validated_data.get('location', {})
        location_instance, _ = Location.objects.get_or_create(**location_data)
        instance.location = location_instance

        # Save the instance
        instance.save()
        return instance


    def create(self, validated_data):
        # Extract location data from the validated data
        location_data = validated_data.pop('location', None)

        # Create Business instance without location
        business_instance = Business.objects.create(**validated_data)

        # Create or update Location instance if location data is provided
        if location_data:
            location_instance, _ = Location.objects.get_or_create(**location_data)
            business_instance.location = location_instance

        # Save the Business instance with the location
        business_instance.save()

        return business_instance
    

class BusinessCategorySerializer(serializers.ModelSerializer):
    businesses = BusinessSerializer(many=True, read_only=True)
    business_category_url = serializers.HyperlinkedIdentityField(
        view_name='category-details',
        lookup_field='pk'
    )
    class Meta:
        model = BusinessCategory
        fields = ['id', 'title', 'businesses', 'business_category_url']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Include related businesses in the serialized data
        representation['businesses'] = BusinessSerializer(instance.businesses.all(), many=True, context=self.context).data
        return representation