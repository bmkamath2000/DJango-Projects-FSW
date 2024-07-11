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

class StudentDetailView(DetailView):
    model = Student
    template_name = 'enrollmentapp/student_detail.html'
    context_object_name = 'students'
    
# Create your views here.
class StudentListView(ListView):
    template_name = 'enrollmentapp/student_list.html'
    model = Student
    context_object_name = 'studentlist'

#or this can be the handler for reg student
class RegisterStudentView(FormView):
    template_name = 'enrollmentapp/register_student.html'
    form_class  = StudentForm
    success_url = '/'
    fields = ['name','usn','courses']
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

