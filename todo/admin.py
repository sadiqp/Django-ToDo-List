from django.contrib import admin
from .models import Tasks


class TaskAdmin(admin.ModelAdmin):
    list_display=['task','status','created_at']
    search_fields=['task']

# Register your models here.
admin.site.register(Tasks,TaskAdmin)