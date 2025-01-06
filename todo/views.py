from django.shortcuts import redirect, render
from .models import Tasks

def addTask(request):
    task = render.POST['task']
    Tasks.objects.create(task=task)
    return redirect('home')