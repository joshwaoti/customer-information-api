from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone
# from django_countries.fields import CountryField


class Customer(models.Model):
    name = models.CharField( max_length=255)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Business_Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Business Categories"

    def __str__(self):
        return self.title

class Location(models.Model):
    county = models.CharField(max_length=255)
    sub_county = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)
    building_name = models.CharField(max_length=255, blank=True)
    floor = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.county} -- {self.sub_county} -- {self.ward}'
    

class Business(models.Model):
    category = models.ForeignKey(Business_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    registration_date = models.DateField()
    age = models.PositiveIntegerField(editable=False)

    
    class Meta:
        verbose_name_plural = "Businesses"

    def __str__(self):
        return self.name
    
    def calculate_age(self):
        return (timezone.now().date() - self.registration_date).days // 365.25
    
    @property
    def calculated_age(self):
        years = self.calculate_age()
        return f"{years} years"

    def save(self, *args, **kwargs):
        self.age = self.calculate_age()
        super().save(*args, **kwargs)

