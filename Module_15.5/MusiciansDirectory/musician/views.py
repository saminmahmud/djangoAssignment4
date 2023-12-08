from django.shortcuts import render,redirect
from . import forms
from .forms import MusicianForm
from . import models
def add_musician(request,id):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician',id=id)
    else:
        musician_form = MusicianForm()
    return render(request, 'musician.html', {'form': musician_form})


def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
        
    return render(request, 'album.html', {'form': musician_form})


def delete_musician (request,id):
    musician = models.Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')