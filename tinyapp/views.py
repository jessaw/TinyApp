# from django.shortcuts import render

# # Create your views here.
# from django.views.generic import CreateView,ListView,DetailView,View,DeleteView,UpdateView
# from django.contrib.auth.views import LoginView
# from .models import User, Url
# from .forms import UrlCreateForm, UserRegisterForm
# from django.forms import ModelForm, TextInput
# import random
# import string
# from datetime import date 
# from django.http import HttpResponseRedirect, HttpResponseForbidden
# from django.urls import reverse

# class UserRegistrationView(CreateView):
#     form_class = UserRegisterForm
#     success_url = '/login'
#     template_name = 'register.html'
#     def form_valid(self, form):
#         self.request.session['username'] = form.cleaned_data['username']
#         return super().form_valid(form)

# class UrlListView(ListView):
#     model= Url
#     context_object_name = 'urls'
#     def get_queryset(self):
#         current_user_id = self.request.user.id
#         if current_user_id == None:
#             return None 
#         return Url.objects.filter(user_id = current_user_id)

#     template_name = 'urls_index.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# class UrlModelForm(ModelForm):
#     class Meta:
#         model = Url
#         fields = ['long_url']
#         widgets = {
#             'long_url': TextInput(attrs={'placeholder': 'http://'})
#         }

# class UrlCreateView(CreateView):
#     form_class = UrlModelForm
#     success_url = '/urls/'
#     template_name = 'urls_new.html'
    
#     def shortURLCreator(self):
#         x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#         return x
#     def form_valid(self, form):
#         current_user_id = self.request.user.id
#         user = User.objects.filter(pk = current_user_id).first()
#         # User.objects.first()
#             # username = 'jess').values_list('id')
#         form.instance.user = user
#         form.instance.short_url = self.shortURLCreator()
#         form.instance.date_created = date.today()
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['username'] = self.request.session.get('username')
        
#         return context

# class UrlDetailView(DetailView):
#     model = Url
#     template_name= 'urls_detail.html'


# class UrlRedirectView(DetailView):
#     def get(self, request, short_url):
#         url=Url.objects.get(short_url = short_url)
#         # long= Url.objects.values_list('long_url', flat= True).get(short_url = short_url)
       
#         return HttpResponseRedirect(url.long_url)
#         # 
# class UrlDeleteView(DeleteView):
#     model = Url
#     success_url = '/urls'

# class UrlUpdateView(UpdateView):
#     model = Url
#     fields = ['long_url']
#     success_url = '/urls'
#     template_name = 'urls_detail.html'

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
        
#         logged_in_user = self.request.session.get('username')
#         logged_in_user_id = None
#         print(logged_in_user)
        
#         if logged_in_user:
#             logged_in_user_id = User.objects.filter(username=logged_in_user)[0].id

#         if(self.object.user_id != logged_in_user_id):
#             return HttpResponseForbidden()
        
#         return super().get(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['username'] = self.request.session.get('username') # Set cookie in the context object
#         print(context['username'])
#         return context


# class UserLoginView(LoginView):
#     success_url = '/urls'
#     def form_valid(self, form):
#         self.request.session['username'] = form.cleaned_data['username']
#         return super().form_valid(form)