from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=1000)
