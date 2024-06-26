from django.urls import path, include
from . import views
urlpatterns = [
    path('addstudent/', views.addStudent),
    path('addcourse/', views.addCourse),
    path('viewstudent/', views.viewStudent),
    path('viewcourse/', views.viewCourse),
    path('addenrollment/', views.addEnrollment),
    path('viewenrollment/', views.viewEnrollment),
]