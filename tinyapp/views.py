from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView
from .models import User
from .forms import UserRegisterForm

class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = '/register'
    template_name = 'register.html'

class UrlListView(ListView):
    model= 'url'
    context_object_name = 'urls'
    queryset = [{'short_url': 'b2xVn2', 'long_url': 'https://www.google.com'}]
    template_name = 'urls_index.html'

