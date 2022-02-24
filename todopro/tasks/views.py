from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import *
# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    context = {"tasks": tasks}

    return render(request, 'home.html', context)





