from django import forms
from .models import Course, Student, Enrollment

class inputformStudent(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','regno']

class inputformCourse(forms.ModelForm):
    class Meta:
        model=Course
        fields=['coursecode','coursetitle']

class inputEnrollment(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields=['regno','coursecode']