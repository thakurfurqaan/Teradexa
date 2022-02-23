from django.db import models

# Create your models here.

class Product(models.Model):
     name = models.CharField(default="", max_length=255)
     weight = models.FloatField(default=0.0)
     price = models.FloatField(default=0.0)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
