from django.db import models

# Create your models here.
class fruitlist(models.Model):
    fruit = models.CharField(max_length=30)

class studentlist(models.Model):
    name = models.CharField(max_length=40)