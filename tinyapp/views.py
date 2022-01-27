from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView
from .models import User, Url
from .forms import UrlCreateForm, UserRegisterForm
from django.forms import ModelForm, TextInput
import random
import string, datetime

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
    success_url = '/urls'
    template_name = 'urls_new.html'
    
    def shortURLCreator(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return x
    def form_valid(self, form):
        user = User.objects.filter(username = 'jess')
        form.instance.user = user
        form.instance.short_url = self.shortURLCreator()
        form.instance.date_created = datetime.today()
        return super().form_valid(form)
# def post(self, request):
#         form = self.form_class(request.POST)
#         return self.form_valid(self.form)