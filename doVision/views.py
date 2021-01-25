from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("doVision app ver.: 0.1")