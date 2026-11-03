from django.db import models

# Create your models here.

class contactsmodel(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField(max_length=30)
    Message=models.TextField()