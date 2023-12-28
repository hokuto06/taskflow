from django.db import models
from django.contrib.auth.models import User

class TasksList(models.Model):

    task_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_description = models.CharField(max_length=50, null=True)
    task_content = models.TextField(max_length=150, null=True)
    task_type = models.CharField(max_length=150, null=True, blank=True)
    status = models.IntegerField( null=True, blank=True)
    deadline = models.DateTimeField()
    open = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.task_name}'

class SubTask(models.Model):

    sub_task = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    open = models.BooleanField() # Este campo debio llamarse "Open" 
    sub_task_list = models.ForeignKey(TasksList, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    state = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return f'{self.sub_task}'