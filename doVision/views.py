from django.contrib.auth.decorators import login_required

from doVision.models import Task
from doVision.forms import TaskForm

from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    my_dict = {'insert_tag': ''}
    return render(request, 'home.html', context=my_dict)


@login_required
def listas(request):
    tasks = (
        Task.objects.
        filter(user=request.user).
        order_by('-prior', '-created')
    )
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')

    context = {'tasks': tasks, 'form': form}
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


def completed_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('TodoList')
