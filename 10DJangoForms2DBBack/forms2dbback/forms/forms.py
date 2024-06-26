from django import forms
from .models import Student

class inputformStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'regno']
