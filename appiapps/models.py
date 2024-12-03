from django.db import models

# Create your models here.

class BusinessDetails(models.Model):
    business_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    create_work_space_name= models.CharField(max_length=100)
    def __str__(self):
        return self.business_name
