from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView,DetailView,View
from .models import User, Url
from .forms import UrlCreateForm, UserRegisterForm
from django.forms import ModelForm, TextInput
import random
import string
from datetime import date 
from django.http import HttpResponseRedirect
from django.urls import reverse

class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = '/register'
    template_name = 'register.html'

class UrlListView(ListView):
    model= 'url'
    context_object_name = 'urls'
    queryset = [{'short_url': 'b2xVn2', 'long_url': 'https://www.google.com'}]
    template_name = 'urls_index.html'


class UrlModelForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        widgets = {
            'long_url': TextInput(attrs={'placeholder': 'http://'})
        }

class UrlCreateView(CreateView):
    form_class = UrlModelForm
    success_url = '/urls/'
    template_name = 'urls_new.html'
    
    def shortURLCreator(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return x
    def form_valid(self, form):
        user = User.objects.first()
            # username = 'jess').values_list('id')
        form.instance.user = user
        form.instance.short_url = self.shortURLCreator()
        form.instance.date_created = date.today()
        return super().form_valid(form)

class UrlDetailView(DetailView):
    model = Url
    template_name= 'urls_detail.html'


class UrlRedirectView(DetailView):
    def get(self, request, short_url):
        url=Url.objects.get(short_url = short_url)
        # long= Url.objects.values_list('long_url', flat= True).get(short_url = short_url)
       
        return HttpResponseRedirect(url.long_url)
        # 