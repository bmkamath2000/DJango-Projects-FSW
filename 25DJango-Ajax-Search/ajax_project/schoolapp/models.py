from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name

class Course(models.Model):
    course_name = models.CharField(max_length=30)
    enrollments = models.ManyToManyField(Student)
    def __str__(self):
        return self.course_name
