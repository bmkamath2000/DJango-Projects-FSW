from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Course
from django.db.models import Q

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

def search_page(request):
    return render(request, 'schoolapp/search_page.html', {})


def search(request):
    name = request.GET.get('name')
    students = Student.objects.filter(Q(**{'first_name__icontains':name}) | Q(**{'last_name__icontains':name})).values('id', 'first_name', 'last_name')
    for s in students:
        courses = Course.objects.filter(**{'enrollments': s['id']}).values()
        s['courses'] = list(courses)
    return JsonResponse(list(students), safe=False)

