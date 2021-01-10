from django.db import models


# Create your models here.
class Task():
    content = models.CharField(max_length=255, default='NaN')
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


class Test():
    task_id = models.ForeignKey(Task, on_delete=Task)
    content = models.CharField(max_length=255, default='NaN')
    created_date = models.DateTimeField(auto_now_add=True)
