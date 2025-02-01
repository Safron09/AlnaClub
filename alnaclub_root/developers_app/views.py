from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import Project
from .forms import ProjectForm

def developers(request):
    return render(request, 'developers_app/developers.html')

def is_superadmin(user):
    return user.is_superuser  # Only SuperAdmin can access

@login_required
def developers(request):
    # Allow SuperAdmins to access the Developers page
    if request.user.is_superuser:
        projects = Project.objects.all()  # SuperAdmin can see all projects
        return render(request, 'developers_app/developers.html', {'projects': projects})

    # Allow Developers and Dual users to access their own projects
    if request.user.role in ['Developer', 'Dual']:
        projects = Project.objects.filter(developer=request.user)
        return render(request, 'developers_app/developers.html', {'projects': projects})

    # Deny access to others
    return HttpResponseForbidden("You are not authorized to view this page.")

@login_required
def add_project(request):
    # Allow SuperAdmin to add projects
    if request.user.is_superuser:
        return render(request, 'developers_app/add_project.html', {'form': ProjectForm()})

    # Allow Developers and Dual users to add projects
    if request.user.role in ['Developer', 'Dual']:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.developer = request.user
                project.save()
                return redirect('developers')
        else:
            form = ProjectForm()

        return render(request, 'developers_app/add_project.html', {'form': form})

    return HttpResponseForbidden("You are not authorized to perform this action.")

@login_required
def update_project(request, project_id):
    # Allow SuperAdmin to update any project
    if request.user.is_superuser:
        project = get_object_or_404(Project, id=project_id)  # No restriction on developer
    else:
        project = get_object_or_404(Project, id=project_id, developer=request.user)  # Restrict for normal users

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('developers')

    else:
        form = ProjectForm(instance=project)

    return render(request, 'developers_app/update_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, project_id):
    # Allow SuperAdmin to delete any project
    if request.user.is_superuser:
        project = get_object_or_404(Project, id=project_id)  # No restriction on developer
    else:
        project = get_object_or_404(Project, id=project_id, developer=request.user)  # Restrict for normal users

    if request.method == 'POST':
        project.delete()
        return redirect('developers')

    return render(request, 'developers_app/delete_project.html', {'project': project})

@login_required
@user_passes_test(is_superadmin)
def superadmin_dashboard(request):
    """SuperAdmin can see all Pending projects"""
    pending_projects = Project.objects.filter(status="Pending")
    return render(request, 'developers_app/superadmin_dashboard.html', {'pending_projects': pending_projects})

@login_required
@user_passes_test(is_superadmin)
def approve_project(request, project_id):
    """SuperAdmin approves a project"""
    project = get_object_or_404(Project, id=project_id)
    project.approve()
    return redirect('superadmin_dashboard')

@login_required
@user_passes_test(is_superadmin)
def reject_project(request, project_id):
    """SuperAdmin rejects a project"""
    project = get_object_or_404(Project, id=project_id)
    project.reject()
    return redirect('superadmin_dashboard')