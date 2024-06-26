from django import forms
from .models import Student
class inputform(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','usn']
