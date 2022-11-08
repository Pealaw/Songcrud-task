from django.shortcuts import render
from django.http import HttpResponse
from .models import musicapp
# Create your views here.


def index(request):
    # musicapp = musicapp.object.all()
    context = {"musicapp": musicapp}
    return render(request, 'musicapp/list_musicapp.html')

    # return HttpResponse("Hello, world. Welcome to musicapp index.")
