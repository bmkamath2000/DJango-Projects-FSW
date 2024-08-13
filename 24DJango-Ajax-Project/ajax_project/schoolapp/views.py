from django.shortcuts import render
# Create your views here.
from .models import Student
from django.http import JsonResponse

def main(request):
    students = Student.objects.all()
    ctx = {'students':students}
    return render(request, 'schoolapp/main.html', ctx)

def register(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    student = Student.objects.create(first_name=first_name, last_name=last_name)
    student.save()
    return JsonResponse({'id': student.id})
