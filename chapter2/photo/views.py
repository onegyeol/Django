from django.shortcuts import get_object_or_404, render
from .models import Photo
from .forms import PhotoForm

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos':photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    print(photo.author)
    return render(request, 'photo/photo_detail.html', {'photo': photo})

def photo_post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else :
        form = PhotoForm()
    
    return render(request, 'photo/photo_post.html', {'form':form})