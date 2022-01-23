from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import User
from .forms import UserRegisterForm

class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = '/register'
    template_name = 'register.html'