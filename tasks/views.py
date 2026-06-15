from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Task
from .forms import TaskForm


# 📊 DASHBOARD + TASK LIST
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'task_list.html', {
        'tasks': tasks,
        'total': tasks.count(),
        'completed': tasks.filter(completed=True).count(),
        'pending': tasks.filter(completed=False).count(),
    })


# ➕ CREATE TASK
@login_required
def task_create(request):
    form = TaskForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task created successfully 🚀")
            return redirect('task_list')

    return render(request, 'task_form.html', {'form': form})


# ✏️ UPDATE TASK
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    form = TaskForm(request.POST or None, instance=task)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully ✏️")
            return redirect('task_list')

    return render(request, 'task_form.html', {'form': form})


# 🗑 DELETE TASK
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.delete()
    messages.success(request, "Task deleted 🗑")
    return redirect('task_list')


# ✔ TOGGLE COMPLETE
@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


# 🔐 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('task_list')

        messages.error(request, "Invalid credentials ❌")

    return render(request, 'login.html')


# 📝 REGISTER
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match ❌")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists ❌")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Account created successfully 🎉")
        return redirect('login')

    return render(request, 'register.html')