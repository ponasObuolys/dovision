from datetime import timezone

from django.shortcuts import render, redirect
from django.http import HttpResponse
from doVision.models import Task
from doVision.forms import TaskForm
from django.utils.timezone import localdate, localtime

# Create your views here.


def index(request):
    my_dict = {'insert_tag': ''}
    return render(request, 'home.html', context=my_dict)


def listas(request):
    tasks = Task.objects.all()
    form = TaskForm()
    now = localdate().strftime('%Y/%m/%d, %A')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form, 'now': now}
    return render(request, 'home.html', context)


def updateTask(request, pk):  # pk = primaty key
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
