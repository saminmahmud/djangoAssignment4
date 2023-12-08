from django.db import models
# from taskModel.models import Task
class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName