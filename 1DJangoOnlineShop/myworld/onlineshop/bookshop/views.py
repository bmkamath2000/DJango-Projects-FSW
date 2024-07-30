from django.shortcuts import render
from .models import Item_list, bookshop # Import your model
from django.template import Template, Context

def authorlist(request):
    # Write your query here
    data = bookshop.objects.all()  # Example query
    # Pass the data to the template context
    context = {'data': data}
    # Render the template with the context
    return render(request, 'db_template.html', context)

# Create your views here.
def booklist(request):
    return render(request, 'basic_template.html' ,{'item_list': Item_list.book_list})

def studlist(request):
    return render(request, 'basic_template.html' ,{'item_list': Item_list.student_list})

def fruitlist(request):
    return render(request, 'basic_template.html' ,{'item_list': Item_list.fruit_list})

