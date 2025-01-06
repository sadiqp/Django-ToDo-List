from django.shortcuts import render

from todo.models import Tasks

# Create your views here.
def home(request):
    tasks= Tasks.objects.filter(status=False)
    context = {'tasks':tasks}
    return render(request,'home.html',context)