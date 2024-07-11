from django.shortcuts import render
from .models import Projects, Languages
from django.views.generic import DetailView, ListView
# Create your views here.
class viewProjectDetails(DetailView):
    template_name = "trackingapp/project_details.html"
    model = Projects
    context_object_name = "projects"

class ProjectList(ListView):
    template_name = "trackingapp/project_list.html"
    model = Projects
    context_object_name = "projects"
