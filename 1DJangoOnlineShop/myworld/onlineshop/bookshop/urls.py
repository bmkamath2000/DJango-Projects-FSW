from django.urls import path
from . import views

urlpatterns = [
    path('booklist',views.booklist),
    path('studlist',views.studlist),
    path('fruitlist',views.fruitlist),
    path('authorlist',views.authorlist),
]


