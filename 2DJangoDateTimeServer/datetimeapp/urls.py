from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('time/',views.welcometime, name='welcome'),
    path('time/plusminus4',views.plusminus4, name='Now plus minus 4'),
    re_path(r'^time/plus/(\d{1,2})$',views.hoursahead, name='hours ahead'),
]