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

def deleteTask(request,pk):
    task=Tasks.objects.get(id=pk)
    task.delete()
    return redirect('home')

def notcompletedTask(request, pk):
    task=Tasks.objects.get(id=pk)
    task.status=False
    task.save()
    return redirect('home')

def editTask(request,pk):
    task=Tasks.objects.get(id=pk)

    if request.method == 'POST':
        new_task = request.POST['mtask']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task':task
        }
        return render(request,'edit_task.html',context)