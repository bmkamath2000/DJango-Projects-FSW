from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def welcometime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>"% now
    return HttpResponse("Welcome!"+ html)


def hoursahead(request, offset): 
    offset = int(offset) 
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset) 
    html = "In %s hour(s), it will be %s." % (offset, dt) 
    return HttpResponse(html)

def plusminus4(request): 
    offset = 4 
    dtplus4 = datetime.datetime.now() + datetime.timedelta(hours=offset)
    dtminus4 = datetime.datetime.now() - datetime.timedelta(hours=offset)
    html = "%s hour(s) back, it was %s.<br> In %s hour(s), it will be %s." % (offset, dtminus4, offset, dtplus4) 
    return HttpResponse(html)