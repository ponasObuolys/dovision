from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoListForm

# Create your views here.

def index(request):
    my_dict = {'insert_tag': ''}
    return render(request, 'home.html', context=my_dict)


def list_view(request):
    todos = TodoList.objects.all()
    form = TodoListForm()

    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    todos_dict = {'todos': todos, 'form': form}
    return render (request, 'home.html', context=todos_dict)