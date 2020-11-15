from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'


class HomeSinPrivilegios(LoginRequiredMixin,generic.TemplateView):
    login_url = 'bases:login'
    template_name = 'bases/sinprivilegios.html'


class SinPrivilegios(PermissionRequiredMixin,LoginRequiredMixin ):
    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = "redirect_to"


    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser :
            self.login_url = "bases:sin_privilegios"
        return HttpResponseRedirect(reverse_lazy(self.login_url))


