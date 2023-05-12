from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import movie
from .forms import mv_form


def index(request):
    mv = movie.objects.all()

    mv_dict = {
        'mv_list': mv
    }

    return render(request, 'index.html', mv_dict)


def details(request, movie_id):
    MV = movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': MV})


def add_field(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']

        mvs = movie(name=name, desc=desc, year=year, img=img)
        mvs.save()

    return render(request, 'add.html')


def update(request, id):
    mv = movie.objects.get(id=id)
    form = mv_form(request.POST or None, request.FILES, instance=mv)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': mv})


def delete(request, id):
    if request.method == 'POST':
        mv = movie.objects.get(id=id)
        mv.delete()
        return redirect('/')
    return render(request, 'delete.html')

