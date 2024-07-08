from django.shortcuts import render, redirect
from enrollmentapp.forms import StudentForm
from django.views import View
from django.views.generic import(
    #display
    TemplateView,
    ListView,
    DetailView,


    #edit 
    FormView,
    CreateView,
    UpdateView,
    DeleteView
)
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

def CourseDetailView(request, courseid):
    course = Course.objects.get(id=courseid)
    students = Student.objects.filter(courses=course)
    return render(request, 'enrollmentapp/course_detail.html', 
    {'course': course, 'students': students})

# Create your views here.
class CourseListView(ListView):
    template_name = 'enrollmentapp/course_list.html'
    model = Course
    context_object_name = 'courselist'


class RegisterStudentView(FormView):
    template_name = 'enrollmentapp/register_student.html'
    form_class  = StudentForm
    success_url = '/'
    fields = ['name','courses']
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

