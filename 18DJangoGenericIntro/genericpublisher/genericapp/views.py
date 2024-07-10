from django.shortcuts import render

# Create your views here.
# views.py
from django.views.generic import ListView, DetailView
from genericapp.models import Publisher

class PublisherListView(ListView):
    model = Publisher

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'genericapp/publisher_detail.html'
    context_object_name = "publisher"