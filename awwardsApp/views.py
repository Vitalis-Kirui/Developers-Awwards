from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Profile, Project, Rates
from django.contrib.auth.models import User
from awwardsApp.forms import ProjectForm,RatingsForm,SignUpForm, UpdateProfileForm, UpdateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

#APIS
from .models import Profile, Project, Rates
from .serializers import ProfileSerializer, ProjectSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    profile = Profile.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {"profile": profile, "projects": projects})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'project' in request.GET and request.GET['project']:
        project = request.GET.get("project")
        results = Project.search_project(project)
        message = f'project'
        return render(request, 'search.html', {'projects': results, 'message': message})
    else:
        message = "You haven't searched for anything, please try again"
    return render(request, 'search.html', {'message': message})

def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.profile.birth_date = form.cleaned_data.get('full_name')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user=current_user.id).all
    return render(request, 'registration/profile.html', {"projects": projects})

@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    profile_object = get_object_or_404(Profile, user_id=id)
    user_object = get_object_or_404(User, id=id)
    profile_form = UpdateProfileForm(request.POST or None, request.FILES, instance=profile_object)
    user_form = UpdateUserForm(request.POST or None, instance=user_object)
    if profile_form.is_valid() and user_form.is_valid():
        profile_form.save()
        user_form.save()
        return HttpResponseRedirect("/profile")

    return render(request, "registration/update_profile.html", {"form": profile_form, "form2": user_form})

@login_required(login_url='/accounts/login')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post_project = form.save(commit=False)
            post_project.user = current_user
            post_project.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'projects.html', {"form": form})

@login_required(login_url='/accounts/login')
def project(request, id):
    project = Project.objects.get(id=id)
    reviews = Rates.objects.all()
    return render(request, 'view-project.html', {"project": project, "reviews": reviews})

@login_required(login_url='/accounts/login')
def view_project(request, id):
    project = Project.objects.get(id=id)
    rate = Rates.objects.filter(user=request.user, project=project).first()
    ratings = Rates.objects.all()
    rating_status = None
    if rate is None:
        rating_status = False
    else:
        rating_status = True
    current_user = request.user
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Rates()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (
                review.design + review.usability + review.content)/3
            review.save()
            return HttpResponseRedirect(reverse('view_project', args=(project.id,)))
    else:
        form = RatingsForm()
    params = {
        'project': project,
        'form': form,
        'rating_status': rating_status,
        'reviews': ratings,
        'ratings': rate

    }
    return render(request, 'view-project.html', params)

class ProfileList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProjectList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)