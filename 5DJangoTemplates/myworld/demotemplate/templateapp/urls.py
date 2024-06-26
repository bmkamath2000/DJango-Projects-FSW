from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.demo, name="demo"),
    path('booklist/', views.booklist, name="book list"),
    path('hellotemp/', views.hellotemplates, name="Hello User"),
    path('hellouser/', views.hellouser, name="Hello sally"),
]