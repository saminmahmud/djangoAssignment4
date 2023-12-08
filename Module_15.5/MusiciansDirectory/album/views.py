from django.shortcuts import render,redirect
from . import forms
from .forms import AlbumForm
from . import models
def add_album(request,id):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album' ,id=id)
    else:
        album_form = AlbumForm()
    return render(request, 'album.html', {'form': album_form})


def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album) 
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
        
    return render(request, 'album.html', {'form': album_form})