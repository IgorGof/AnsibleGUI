from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

menu =[{'title': "Хосты", 'url_name': 'arms'},
        {'title': "Задачи", 'url_name': 'tasks'}, 
        {'title': "Расписания", 'url_name': 'schedules'},
        {'title': "Вход", 'url_name': 'login'}]

def arms(request):
    arms = ARM.objects.all()
    context = {
        'arms': arms,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'runner/index.html', context=context)

def tasks(request):
    return HttpResponse("Задачи") 

def schedules(request):
    return HttpResponse("Расписания") 

def login(request):
    return HttpResponse("Авторизация") 

