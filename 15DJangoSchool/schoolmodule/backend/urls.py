from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.home),
    path('generateregno/', views.generate_reg_no),
    path('enroll/',views.enroll)
]
