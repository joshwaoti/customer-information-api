from dateutil.relativedelta import relativedelta
from django.db import models
from django_countries.fields import CountryField


class Customer(models.Model):
    name = models.CharField( max_length=255)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()
    date_of_birth = models.DateField()
    nationality = CountryField()

    def __str__(self):
        return self.name
    
class Business_Category(models.Model):
    title = models.CharField(max_length=255)


class Location(models.Model):
    county = models.CharField(max_length=255)
    sub_county = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    building_name = models.CharField(max_length=255, blank=True)
    floor = models.IntegerField(blank=True)

class Business(models.Model):
    category = models.ForeignKey(Business_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    registration_date = models.DateField()
    age = models.PositiveIntegerField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.age = (models.DateField.today() - self.registration_date).days // 365.25
        super().save(*args, **kwargs)