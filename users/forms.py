from users.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


