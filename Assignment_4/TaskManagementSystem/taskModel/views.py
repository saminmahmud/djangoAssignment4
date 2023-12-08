from django.shortcuts import render,redirect
from .forms import TaskForm
from . import models

def add_task(request,id):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show' )
    else:
        task_form = TaskForm()
    return render(request, 'task.html', {'form': task_form})

def edit_task(request,id):
    task = models.Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show')
        
    return render(request, 'task.html', {'form': task_form})

def delete_task (request,id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('show')