from django.db import models

class Languages(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

# Create your models here.
class Projects(models.Model):
    topic = models.CharField(max_length = 40)
    languages = models.ManyToManyField(Languages,related_name='languages')
    duration_days = models.IntegerField()
    def __str__(self):
        return self.topic