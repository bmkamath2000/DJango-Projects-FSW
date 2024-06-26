from django.urls import path
from . import views
urlpatterns = [
    path('students/', views.stud_list),
    path('fruits/', views.fruit_list),
]