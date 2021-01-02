from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=100, default="India")

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products", null=True
    )
    name = models.CharField(
        max_length=40,
    )
    added_at = models.DateField()

    def __str__(self):
        return self.name
