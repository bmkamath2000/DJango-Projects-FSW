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
#Either this can be the handler for reg student
def register_student(request):
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request,'enrollmentapp/register_student.html',{'form':form})

class CourseDetailView(DetailView):
    model = Course
    template_name = 'enrollmentapp/course_detail.html'
    context_object_name = 'courses'
    
# Create your views here.
class CourseListView(ListView):
    template_name = 'enrollmentapp/course_list.html'
    model = Course
    context_object_name = 'courselist'

#or this can be the handler for reg student
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

