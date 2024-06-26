from django.shortcuts import render
from .models import fruitlist, studentlist
from django.template import Template, Context
# Create your views here.
def stud_list(request):
    students = studentlist.objects.all()
    c1 = {'students':students}
    return render(request, 'db_template_student.html', c1)

def fruit_list(request):
    fruits = fruitlist.objects.all()
    c2 = {'fruits':fruits}
    return render(request, 'db_template_fruit.html', c2)