from django.shortcuts import render, get_object_or_404, redirect
from .models import Album

def album(request):
    albums = Album.objects
    return render(request, 'album.html', {'albums':albums})

def detailshot(request, image_id):
    details = get_object_or_404(Album, pk = image_id)
    return render(request, 'detailshot.html', {'detail':details})

def create(request):
    album = Album()
    album.image = request.FILES['image']
    album.save() 
    return redirect('album') 

def deleteimg(request, image_id):
    post = get_object_or_404(Album, pk = image_id)
    post.delete()
    return redirect('album')