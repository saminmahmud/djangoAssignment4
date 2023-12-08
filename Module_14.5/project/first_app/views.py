from django.shortcuts import render
from .forms import ExampleForm , StudentForm
from . import models

def index(request):
    if request.method == "POST":
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExampleForm()
    return render(request, 'index.html', {'form': form })

def index_two(request):
    std = StudentForm()
    return render(request, 'another.html', {'form': std})
    # MyModel =models.MyModel.objects.all()
    # return render(request, 'another.html', {'data': MyModel})