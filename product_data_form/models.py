from django.db import models

class Market(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.date}"


class Product(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, blank=True, null=True)
    number = models.CharField(max_length=200, blank=True)
    brand_name = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200, blank=True)
    model_number = models.CharField(max_length=200, blank=True)
    serial_number = models.CharField(max_length=200, blank=True)
    material_color = models.CharField(max_length=200, blank=True)
    condition = models.CharField(max_length=200, blank=True)
    detail = models.TextField(blank=True)
    price = models.CharField(max_length=200, blank=True)
    winning_bid = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
