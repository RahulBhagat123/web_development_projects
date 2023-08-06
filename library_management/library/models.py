#importing relevant packages/modules
from django.db import models

# Create your models here.
# model for adding book
class add_book(models.Model):   
    book_name=models.CharField(max_length=20)
    book_serial_number=models.IntegerField(primary_key=True)
    rented=models.IntegerField(default=0)

# model for adding user
class add_user(models.Model):   
    user_name=models.CharField(max_length=35)
    email=models.EmailField(max_length=40)
    phone_number=models.IntegerField(default=10)
    book_serial_number=models.CharField(max_length=20)
    cost_per_day=models.IntegerField(default=0)
    days_of_rent=models.IntegerField(default=0)