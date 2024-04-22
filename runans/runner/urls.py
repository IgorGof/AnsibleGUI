from django.urls import path, include

from .views import *

urlpatterns = [
    path('', arms, name='arms'),
    path('tasks/', tasks, name='tasks'), 
    path('schedules/', schedules, name='schedules'),
    path('login/', login, name='login'),
]

