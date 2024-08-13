from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
import csv  
from .models import Projects, Languages
from django.views.generic import DetailView, ListView

# Create your views here.
class viewProjectDetails(DetailView):
    template_name = "pdfcsvapp/project_details.html"
    model = Projects
    context_object_name = "projects"

class ProjectList(ListView):
    template_name = "pdfcsvapp/project_list.html"
    model = Projects
    context_object_name = "projects"
 
def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), 
                            as_attachment=True, 
                            filename='Project_catalog.pdf')
    return response
 
 
def generate_pdf_file():
    from io import BytesIO
 
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
 
    # Create a PDF document
    projects = Projects.objects.all()
    p.drawString(100, 750, "Projects List")
    i = 1
    y = 700
    for project in projects:
        p.drawString(100, y, "(%s)"% i)
        p.drawString(100, y - 20, f"Topic: {project.topic}")
        languagesall = ""
        for language in project.languages.all():
            languagesall = languagesall + "," + language.__str__()
        p.drawString(100, y - 40, f"Languages: {languagesall}")
        p.drawString(100, y - 60, f"Duration: {project.duration_days}")
        y -= 80
        i = i + 1
 
    p.showPage()
    p.save()
 
    buffer.seek(0)
    return buffer

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="books.csv"'  
    projects = Projects.objects.all()  
    writer = csv.writer(response)  
    for project in projects:  
        languagesall = ""
        for language in project.languages.all():
            languagesall = languagesall + "," + language.__str__()
        writer.writerow([project.topic,languagesall,project.duration_days])  
    return response 