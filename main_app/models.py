from django.db import models

# Create your models here.

class userinfo(models.Model):
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    email=models.EmailField()
    phone_number=models.CharField(max_length=255)
    is_active=models.BooleanField(null=True)
