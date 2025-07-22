from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Bird

def home(request):
    return render(request,"index.html",{"name":"index"})

def birds_view(request):
    birds = Bird.objects.all()
    return render(request, 'birds.html', {'birds': birds})


def bird_detail_view(request, pk):
    bird = get_object_or_404(Bird, pk=pk)
    return render(request, 'bird_detail.html', {'bird': bird})