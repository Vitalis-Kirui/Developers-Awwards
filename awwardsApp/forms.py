from awwardsApp.models import Profile, Project, Rates
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contact','profile_pic', 'bio']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'profile', 'date']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ['design', 'usability', 'content']