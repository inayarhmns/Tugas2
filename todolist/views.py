from pdb import post_mortem
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from todolist.forms import CreateTaskForm

# Create your views here.

title_list = []
desc_list = []
@login_required(login_url='/todolist/login/')  
def show_todolist(request):
    todolists = Task.objects.all()
    context = {
    'nama' : 'Inaya Rahmanisa',
    'npm'  : '2106708330',
    'todolists' : todolists,
    'username' : request.user,
    
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist')) # membuat response
            response.set_cookie('username', username) #
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')  
def create_task(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            form.save()
            
        else:
            messages.info(request, 'Fields cannot be empty!')
    context = {'form':form}
    return render(request, 'create_task.html', context)

