from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_tag': ''}
    return render(request, 'home.html', context=my_dict)