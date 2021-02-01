from django.shortcuts import render, redirect
from .models import TodoList

# Create your views here.

def index(request):
    my_dict = {'insert_tag': ''}
    return render(request, 'home.html', context=my_dict)


def list(request):
    todos = TodoList.objects.order_by('text')
    todos_dict = {'todos': todos}
    # if request.method == "POST":
        # if "taskAdd" in request.POST:
        #     title = request.POST['text']
        #     Todo = TodoList(text=title, complete=False)
        #     Todo.save()
        #     return redirect("/")
    return render (request, 'home.html', context=todos_dict)