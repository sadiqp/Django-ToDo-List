from django.db import models

# Create your models here.
class Tasks(models.Model):
    task=models.CharField(max_length=250)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task