from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile, Project, Rates

# Create your views here.
def index(request):
    profile = Profile.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {"profile": profile, "projects": projects})

def search(request):
    if 'project' in request.GET and request.GET['project']:
        project = request.GET.get("project")
        results = Project.search_project(project)
        message = f'project'
        return render(request, 'search.html', {'projects': results, 'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'search.html', {'message': message})