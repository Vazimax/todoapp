from django.shortcuts import render , redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    form = Task_Form()
    if request.method == 'POST':
        form = Task_Form(request.POST)
        if form.is_valid :
            form.save()
        return redirect('/')
    my_context = {
        'tasks' : tasks,
        'form' : form
    }
    return render(request,'base/home.html', my_context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = Task_Form(instance=task)
    if request.method == 'POST':
        form = Task_Form(request.POST , instance = task)
        if form.is_valid():
            form.save()
            return redirect('/')
    my_context = {
        'form' : form
    }
    return render(request,'base/update_task.html',my_context)

def delete(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    my_context = {
        'item' : item
    }
    return render(request,'base/delete.html' , my_context)