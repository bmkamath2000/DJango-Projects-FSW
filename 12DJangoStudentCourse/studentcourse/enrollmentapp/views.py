from django.shortcuts import render, redirect
from enrollmentapp.forms import StudentForm
# Create your views here.

from .models import Course, Student

def register_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('name')
        course_id = request.POST.get('course_id')
        student = Student.objects.create(name=name)
        course = Course.objects.get(id=course_id)
        course.students.add(student)
        return redirect('enrollmentapp/course_detail.html', course_id=course.id)
    
    courses = Course.objects.all()
    return render(request, 'enrollmentapp/register_student.html', {'form': StudentForm, 'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    return render(request, 'enrollmentapp/course_detail.html', {'course': course, 'students': students})




