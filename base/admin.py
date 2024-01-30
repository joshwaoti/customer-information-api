from django.contrib import admin
from .models import Customer, Business, Business_Category, Location

admin.site.register(Customer)
admin.site.register(Business_Category)
admin.site.register(Business)
admin.site.register(Location)