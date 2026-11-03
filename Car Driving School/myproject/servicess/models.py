from django.db import models

# Create your models here.
class servicemodel(models.Model):
    Title=models.CharField(max_length=50)
    Detail=models.TextField()