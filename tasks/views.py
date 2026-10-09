
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def home(request):
    task_list = Task.objects.all()

    context = {
        "username": "Django Student",
        "tasks": task_list,
    }

    return render(request, "tasks/home.html", context)


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()

    return render(request, "tasks/add_task.html", {"form": form})


    
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "tasks/edit_task.html",
        {"form": form, "task": task},
    )