from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup),
    path('add-task/', views.add_task),
    path('done-task/<int:id>', views.done),
    path('logout/', views.logout),
    path('schedule/', views.update_schedule),
]
