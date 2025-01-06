from django.shortcuts import redirect, render
from .models import Tasks

def addTask(request):
    task = request.POST['task']
    Tasks.objects.create(task=task)
    return redirect('home')

def markAsDone(request,pk):
    task=Tasks.objects.get(id=pk)
    task.status=True
    task.save()
    return redirect('home')