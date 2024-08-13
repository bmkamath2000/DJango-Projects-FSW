from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main),
    path('register', views.register, name='register'),
    path('search_page', views.search_page, name='search_page'),
    path('search', views.search, name='search'),
]
