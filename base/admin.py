from django.contrib import admin
from .models import Customer, Business, BusinessCategory, Location

admin.site.register(Customer)
admin.site.register(BusinessCategory)
admin.site.register(Business)
admin.site.register(Location)