from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Project, Task
from .forms import ProjectForm, TaskForm

@login_required
def project_list(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'task_scheduler_app/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    return render(request, 'task_scheduler_app/project_detail.html', {'project': project})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'task_scheduler_app/project_form.html', {'form': form})

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'task_scheduler_app/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'task_scheduler_app/project_confirm_delete.html', {'project': project})

@login_required
def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    tasks = project.tasks.all()
    return render(request, 'task_scheduler_app/task_list.html', {'project': project, 'tasks': tasks})

@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_list', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'task_scheduler_app/task_form.html', {'form': form, 'project': project})

@login_required
def task_update(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    task = get_object_or_404(Task, id=task_id, project=project)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list', project_id=project.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_scheduler_app/task_form.html', {'form': form, 'project': project, 'task': task})

@login_required
def task_delete(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    task = get_object_or_404(Task, id=task_id, project=project)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list', project_id=project.id)
    return render(request, 'task_scheduler_app/task_confirm_delete.html', {'project': project, 'task': task})
