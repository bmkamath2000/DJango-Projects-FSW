from django.db import models
from django.core import exceptions, validators

# Create your models here.
def capital_only(value):
    if value[0].isupper():
        return value
    else:
        raise exceptions.ValidationError("Should be first letter capital")


class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100,
                            validators = [capital_only,])
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.name.lower()



