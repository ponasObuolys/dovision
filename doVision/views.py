from datetime import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from doVision.models import Task
from doVision.forms import TaskForm
from django.utils.timezone import localdate, localtime
from django.db.models import Case, When, F


# Create your views here.


def index(request):
    my_dict = {'insert_tag': ''}
    return render(request, 'home.html', context=my_dict)


def listas(request):
    tasks = Task.objects.order_by('-priority')
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
    get_object_or_404(Task, id=pk)
    if request.method == 'GET':

        Task.objects.filter(id=pk).update(priority=F('priority')+1)

        return redirect('/')
    uzduotys = Task.objects.order_by('-priority')
    context = {'uzduotys': uzduotys}
    return render(request, 'home.html', context=context)

