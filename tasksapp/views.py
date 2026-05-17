from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Task




# Create your views here.

@login_required(login_url='users:login')
def index(request):
    tasks = Task.objects.filter( user=request.user)
    return render(request, "tasksapp/index.html",{
        "tasks": tasks
    })
@login_required(login_url='users:login')
def add(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.tasksfield = request.POST["tasksfield"]
        task.description = request.POST["description"]
        task.save()
        return redirect("tasksapp:index")
    
    return render(request, "tasksapp/index.html")
@login_required(login_url='users:login')    
def delete(request):
    if request.method == "POST":
        task_id = request.POST["id"]
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
        return redirect("tasksapp:index")
    else:
        return HttpResponse("Invalid request method")
    
@login_required(login_url='users:login')
def toggle_complete(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id, user=request.user)
        task.completed = 'completed' if task.completed != 'completed' else 'Not Completed'
        task.save()
        print(task.completed)
    return redirect("tasksapp:index")