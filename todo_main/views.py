from django.shortcuts import render

from todo.models import Tasks

# Create your views here.
def home(request):
    tasks= Tasks.objects.filter(status=False).order_by('-modified_at')
    completed_tasks = Tasks.objects.filter(status=True).order_by('-modified_at')
    context = {
        'tasks':tasks,
        'completed_tasks': completed_tasks,
        }
    return render(request,'home.html',context)