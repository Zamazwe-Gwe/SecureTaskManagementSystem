from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from auditlog.models import AuditLog

@login_required
def task_list(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(owner=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        AuditLog.objects.create(user=request.user, action=f"Created task: {task.title}")
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if not request.user.is_superuser and task.owner != request.user:
        return redirect('task_list')

    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        AuditLog.objects.create(
    user=request.user,
    action=f"Updated task: {task.title}"
)
    
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if not request.user.is_superuser and task.owner != request.user:
        return redirect('task_list')

    task.delete()
    AuditLog.objects.create(user=request.user, action=f"Deleted task: {task.title}")
    return redirect('task_list')
