# cars/models.py
from django.db import models

class Car(models.Model):
    car_id = models.CharField(max_length=255)
    car_name = models.CharField(max_length=255)
    car_brand = models.CharField(max_length=255)  # Ensure this field exists
    car_type = models.CharField(max_length=255)  # Ensure this field exists
    car_year = models.IntegerField()

    def __str__(self):
        return self.car_name
