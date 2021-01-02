from django.contrib import admin
from products.models import Manufacturer, Product

admin.site.register(Product)
admin.site.register(Manufacturer)
