from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello Student/Teacher/Parent</h1>")

def enroll(request):
    return render(request,'backend/index.html',{'string':'path is working'})

@csrf_exempt
def generate_reg_no(request):
    result_response = {'value':1}
    return JsonResponse(result_response)
