from django.shortcuts import render
from .models import Student, Course, Enrollment
# Create your views here.
from .forms import inputformStudent, inputformCourse, inputEnrollment

def addStudent(request):
    if request.method=="POST": 
        form1=inputformStudent(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'index.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputformStudent()
        return render(request,'index.html',{'form':form1})

def addCourse(request):
    if request.method=="POST": 
        form1=inputformCourse(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'index.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputformCourse()
        return render(request,'index.html',{'form':form1})

def addEnrollment(request):
    if request.method=="POST": 
        form1=inputEnrollment(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'index.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputEnrollment()
        return render(request,'index.html',{'form':form1})

def viewStudent(request):
    students = Student.objects.all()
    c1 = {'students':students}
    return render(request, 'db_template_student.html', c1)

def viewCourse(request):
    courses = Course.objects.all()
    c1 = {'courses':courses}
    return render(request, 'db_template_course.html', c1)

def viewEnrollment(request):
    enroll = Enrollment.objects.all()
    c1 = {'enrollments':enroll}
    return render(request, 'db_template_enroll.html', c1)