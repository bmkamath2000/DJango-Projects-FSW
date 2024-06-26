from django.urls import path, include
from . import views
urlpatterns = [
    path('addstudent/', views.addStudent),
    path('stud_list/', views.stud_list),
]
