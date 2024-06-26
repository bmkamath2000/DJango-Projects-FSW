from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    coursecode = models.CharField(max_length=8, primary_key=True)
    coursetitle = models.CharField(max_length=30)
    def __str__(self): 
        return self.coursecode

class Student(models.Model):
    name = models.CharField(max_length=40)
    regno = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return self.name
    # class Meta:
    #     db_table_comment = "Holds info about Students"

class Enrollment(models.Model):
    e_id = models.IntegerField()
    regno = models.ForeignKey( Student,
    related_name = "e_regno",
    on_delete= models.SET_NULL,
    null = True,
    )
    coursecode = models.ForeignKey( Course,
    related_name = "e_coursecode",
    on_delete= models.SET_NULL,
    null = True,
    # db_comment ="Foreign Key to the Course" 
    )
    def __str__(self):
        return self.regno + self.coursecode