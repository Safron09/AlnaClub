from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from developers_app.models import Project

# Create your views here.
@login_required
def investors(request):
    return render(request, 'investors_app/investors.html') 

@login_required
def investors(request):
    # Fetch only projects that have been approved by SuperAdmin
    approved_projects = Project.objects.filter(status="Approved")

    return render(request, 'investors_app/investors.html', {'approved_projects': approved_projects})
