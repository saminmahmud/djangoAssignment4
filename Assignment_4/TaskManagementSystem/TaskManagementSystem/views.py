from django.shortcuts import render
from taskCategory.models import Category
from taskModel.models import Task
def show(request):
    data = Task.objects.all()
    # data2 = Category.objects.all()
    return render(request, 'show.html', {'data': data})