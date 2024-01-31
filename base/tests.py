from datetime import date
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, Business_Category, Location, Business

class CustomerViewSetTests(APITestCase):
    def setUp(self):
        self.customer_data = {
            "name": "John Doe",
            "customer_phone": "123456789",
            "customer_email": "john.doe@example.com",
            "date_of_birth": "1990-01-01",
            "nationality": "US"
        }
        self.customer = Customer.objects.create(**self.customer_data)
        self.customer_url = reverse('customer-details', args=[self.customer.id])

    def test_get_customer_list(self):
        url = reverse('customer-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        url = reverse('customer-list')
        response = self.client.post(url, data=self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

    def test_get_customer_detail(self):
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_customer(self):
        updated_data = {
        "name": "Updated Name",
        "customer_phone": "987654321",  # Provide a valid phone number
        "customer_email": "updated.email@example.com",  # Provide a valid email
        "date_of_birth": "1990-01-01",  # Provide a valid date of birth
        "nationality": "US"  # Provide a valid nationality
    }
        response = self.client.put(self.customer_url, data=updated_data, format='json')
        if response.status_code != status.HTTP_200_OK:
            print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, "Updated Name")

    def test_delete_customer(self):
        response = self.client.delete(self.customer_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)

class BusinessViewSetTests(APITestCase):
    def setUp(self):
        self.category = Business_Category.objects.create(title="Technology")
        self.customer = Customer.objects.create(name="Business Customer", customer_phone="987654321", customer_email="customer@example.com", date_of_birth="1980-01-01", nationality="US")
        self.location_data = {"county": "Mombasa", "sub_county": "Nyali", "ward": "Bamburi", "building_name": "XYZ Tower", "floor": 5}
        self.location = Location.objects.create(**self.location_data)
        
        self.business_data = {
            "category": self.category,
            "name": "Business Name",
            "customer": self.customer,
            "location": self.location,
            "registration_date": date(2022, 1, 1),
        }
        self.business = Business.objects.create(**self.business_data)
        self.business_url = reverse('business-details', args=[self.business.id])

    def test_get_business_list(self):
        url = reverse('business-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_business(self):
        url = reverse('business-list')
        new_business_data = {
            "category": self.category.id,
            "name": "New Business",
            "customer": self.customer.id,
            "location": self.location_data,
            "registration_date": "2022-02-01",
        }
        response = self.client.post(url, data=new_business_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Business.objects.count(), 2)

    def test_get_business_detail(self):
        response = self.client.get(self.business_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_business(self):
        updated_data = {
        "name": "Updated Business",
        "registration_date": "2022-02-01",
        "category": self.category.id,
        "customer": self.customer.id,
        "location": self.location_data
    }
        response = self.client.put(self.business_url, data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.business.refresh_from_db()
        self.assertEqual(self.business.name, "Updated Business")

    def test_delete_business(self):
        response = self.client.delete(self.business_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Business.objects.count(), 0)
