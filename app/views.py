from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout as lg
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from app.forms import TaskForm, ScheduleForm
from app.models import Task, Schedule
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TaskForm()
        schedule = ScheduleForm()
        tasks = Task.objects.filter(user = user)
        context = {
            'form' : form,
            'schedule' : schedule,
            'tasks' : tasks,
        }
        return render(request, 'index.html', context=context)
    else:
        return render(request, 'home.html')

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request, 'login.html', context=context)
    
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {
            "form" : form
            }
            return render(request, 'login.html', context=context)

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

def signup(request):
    if request.method == 'GET':
        form = UserCreateForm()
        context = {
            "form" : form
        }
        return render(request, 'signup.html', context=context)

    else:
        form = UserCreateForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)

@login_required(login_url='login')
def add_task(request):
    if request.user.is_authenticated:
        user = request.user

    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = user
        task.save()
        return redirect("home")
    else:
        context = {
            'form' : form
        }
        return render(request, 'index.html', context=context)

@login_required(login_url='login')
def update_schedule(request):
    return render(request, 'schedule.html')

def done(request, id):
    Task.objects.get(pk = id).delete()
    return redirect('home')

def logout(request):
    lg(request)
    return redirect('login')