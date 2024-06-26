from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Item_list

# Create your views here.
def demo(request):
    return HttpResponse('<h1>Hello World</h1>')

def booklist(request):
    today_is_weekend = True
    return render(request,'Item_template.html',{'item_list':Item_list.book_list,
    'today_is_weekend': today_is_weekend})

def hellotemplates(request):
    t = Template("Hello,{{user}}")
    html = t.render(Context({'user':'Sandesh'}))
    return HttpResponse(html)

def hellouser(request):
    person = {'name': 'sally', 'age': 4} 
    t = Template('{{person.name.upper}} is {{person.age.isdigit}} years old')
    html = t.render(Context({'person': person}))
    return HttpResponse(html)
