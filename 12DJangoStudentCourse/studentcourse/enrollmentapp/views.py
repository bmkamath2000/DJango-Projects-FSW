from django.shortcuts import render, redirect
from enrollmentapp.forms import StudentForm
# Create your views here.

from .models import Course, Student

def register_student(request):
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request,'enrollmentapp/register_student.html',{'form':form})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    students = Student.objects.filter(courses=course_id)
    return render(request, 'enrollmentapp/course_detail.html', {'course': course, 'students': students})




