from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.filter(status='completed').order_by('-completion_date')
    return render(request, 'portfolio/list.html', {'projects': projects})
