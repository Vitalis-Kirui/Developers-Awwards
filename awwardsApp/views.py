from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile, Project, Rates

# Create your views here.
def index(request):
    profile = Profile.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {"profile": profile, "projects": projects})
