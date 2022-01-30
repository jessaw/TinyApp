# from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView,DetailView,View,DeleteView,UpdateView
from django.forms import ModelForm, TextInput
import random
import string
from datetime import date 
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse
from django.shortcuts import render
from tinyapp.models import User, Url

class UrlListView(LoginRequiredMixin,ListView):
    login_url ='/login/'
    model= Url
    context_object_name = 'urls'
    template_name = 'urls_index.html'

    def get_queryset(self):
        current_user_id = self.request.user.id
        if current_user_id == None:
            return None 
        return Url.objects.filter(user_id = current_user_id)

    # cookie info
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') #might need to remove
        return context


class UrlModelForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        widgets = {
            'long_url': TextInput(attrs={'placeholder': 'http://'})
        }

class UrlCreateView(LoginRequiredMixin,CreateView):
    login_url ='/login/'
    form_class = UrlModelForm
    success_url = '/urls/'
    template_name = 'urls_new.html'
    
    # method to get short url
    def shortURLCreator(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return x

    # create URL form
    def form_valid(self, form):
        current_user_id = self.request.user.id
        user = User.objects.filter(pk = current_user_id).first()
        form.instance.user = user
        form.instance.short_url = self.shortURLCreator()
        form.instance.date_created = date.today()
        return super().form_valid(form)

# get cookie 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        
        return context

class UrlDetailView(DetailView):
    model = Url
    template_name= 'urls_detail.html'


class UrlRedirectView(DetailView):
    def get(self, request, short_url):
        url=Url.objects.get(short_url = short_url)
        # long= Url.objects.values_list('long_url', flat= True).get(short_url = short_url)

        key = short_url

        if key in self.request.session.keys():
            self.request.session[key] += 1
        else:
            self.request.session[key] = 1
       
        return HttpResponseRedirect(url.long_url)

#

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') # Set cookie in the context object
        print(context['username'])

class UrlDeleteView(DeleteView):
    model = Url
    success_url = '/urls'

class UrlUpdateView(UpdateView):
    model = Url
    fields = ['long_url']
    success_url = '/urls'
    template_name = 'urls_detail.html'


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        logged_in_user = self.request.session.get('username')
        logged_in_user_id = None
        print(logged_in_user)
        
        if logged_in_user:
            logged_in_user_id = User.objects.filter(username=logged_in_user)[0].id

        if(self.object.user_id != logged_in_user_id):
            return HttpResponseForbidden()
        
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') # Set cookie in the context object
        print(context['username'])
    
        total_visits = str(context['url'])
        visitor_count = str(context)
        if self.request.session.get(total_visits) == None:
            context['total_visits'] = 0
        else:
            context['total_visits'] = self.request.session.get(total_visits)
        
        return context

