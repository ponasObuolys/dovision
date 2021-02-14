from doVision.models import Task
from doVision.forms import TaskForm

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import localdate


# Create your views here.


def index(request):
    my_dict = {'insert_tag': ''}
    return render(request, 'home.html', context=my_dict)


def listas(request):
    tasks = Task.objects.order_by('-prior', '-created')
    form = TaskForm()
    now = localdate().strftime('%Y/%m/%d, %A')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form, 'now': now}
    return render(request, 'home.html', context)


def updateTask(request, pk):  # pk = primary key
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)


def prioritize(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.prior = not task.prior
    task.save()
    return redirect('TodoList')
