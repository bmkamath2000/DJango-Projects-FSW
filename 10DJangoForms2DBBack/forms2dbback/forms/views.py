from django.shortcuts import render
from .models import Student
from .forms import inputformStudent 
from django.template import Template, Context

def addStudent(request):
    if request.method=="POST": 
        form1=inputformStudent(request.POST)
        form1.save()
        return render(request,'index.html',{'form':form1, 'param1':'Success'})
    else:
        form1=inputformStudent()
        return render(request,'index.html',{'form':form1})

def stud_list(request):
    students = Student.objects.all()
    c1 = {'students':students}
    return render(request,'db_template_student.html',c1)