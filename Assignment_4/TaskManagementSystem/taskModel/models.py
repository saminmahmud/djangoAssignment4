from django.db import models
from taskCategory.models import Category
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)


    def __str__(self):
        return self.taskTitle