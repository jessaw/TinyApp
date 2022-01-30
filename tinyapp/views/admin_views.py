from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from tinyapp.models import User


class SeeAdminsView(PermissionRequiredMixin,ListView):
    model= User
    context_object_name = 'users'
    template_name = 'admin.html'
    permission_required = 'tinyapp.view_user'

# Get context data 
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['username'] = self.request.session.get('username') #might need to remove
            return context

    def get_queryset(self):
        current_user_id = self.request.user.id
        if current_user_id == None or self.request.user.has_perm('tinyapp.view_user') == False:
            return None
        return User.objects.all()


