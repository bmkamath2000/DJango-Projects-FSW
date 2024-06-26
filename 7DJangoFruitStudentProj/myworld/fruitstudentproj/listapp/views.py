from django.shortcuts import render
from .forms import inputform
# Create your views here.
def studentform(request):
    if(request.method =="POST"):
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, 'index.html',{'form':form1, 'param1':"success"})
    else:
        form1=inputform()
        return render(request, 'index.html',{'form':form1})