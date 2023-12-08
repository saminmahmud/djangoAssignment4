from django.shortcuts import render,redirect
from .forms import CategoryForm
# Create your views here.
def add_category(request,id):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category' ,id=id)
    else:
        category_form = CategoryForm()
    return render(request, 'category.html', {'form': category_form})

    
