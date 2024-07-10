# urls.py
from django.urls import path
from genericapp.views import PublisherListView, PublisherDetailView

urlpatterns = [
    path("publishers/", PublisherListView.as_view()),
    path("publishers/<int:pk>/",PublisherDetailView.as_view(), name="publishers_detail")
]