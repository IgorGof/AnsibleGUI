from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

menu =["Хосты", "Задачи", "Расписания", "Войти"]
def index(request):
    arms = ARM.objects.all()
    return render(request, 'runner/index.html', {'arms': arms, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'runner/about.html', {'menu': menu, 'title': 'О сайте'})

def tasks(request):
    return redirect('home', permanent=True) 
