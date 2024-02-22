from django.db import models
from datetime import datetime

# Create your models here.
class Booking_table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    BookingDate = models.DateField(default=datetime.now, blank=True)
    
class Menu_table(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
