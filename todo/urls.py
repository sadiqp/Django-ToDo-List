from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_done/<int:pk>/',views.markAsDone,name='mark_as_done'),
    path('deleteTask/<int:pk>/',views.deleteTask,name='deleteTask'),
    path('not_completed_task/<int:pk>/',views.notcompletedTask,name='not_completed_task'),
    path('edit_task/<int:pk>/',views.editTask,name='edit_task'),
]
