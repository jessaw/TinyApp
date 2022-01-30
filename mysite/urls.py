"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tinyapp.views import UserRegistrationView,UserLoginView,SeeAdminsView
from tinyapp.views import UrlListView,UrlCreateView,UrlDetailView, UrlRedirectView,UrlDeleteView,UrlUpdateView
from django.contrib.auth.views import LogoutView,PasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('urls/',UrlListView.as_view(), name = 'urls'),
    path('urls/new/',UrlCreateView.as_view(), name='urls-new'),
    path('urls/<pk>', UrlDetailView.as_view(), name='urls-detail'),
    path('u/<short_url>', UrlRedirectView.as_view(), name='urls-redirect'),
    path('urls/delete/<pk>', UrlDeleteView.as_view(), name= 'urls-delete'),
    path('urls/edit/<pk>', UrlUpdateView.as_view(), name= 'urls-edit'),
    path('login/',UserLoginView.as_view(), name = 'login'),
    path('logout/',LogoutView.as_view(), name='user_logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', PasswordChangeView.as_view()),
    path('', UrlListView.as_view(), name = 'main'),
    path('userlist/', SeeAdminsView.as_view(), name = 'userlist')
]


