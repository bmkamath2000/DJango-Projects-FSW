from django.urls import path, include
from . import views

urlpatterns = [
    path('tracking/<int:pk>/', views.viewProjectDetails.as_view(), name='project_detail'),
    path('tracking/', views.ProjectList.as_view()),
	path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('generate-csv/', views.getfile, name='generate_csv'),
]
