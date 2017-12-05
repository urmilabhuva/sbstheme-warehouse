# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from dashboard.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "pages/blank.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'title': "Dashboard"})
        
        return context

    

        

    

class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = "pages/sign-in.html"
    success_url = reverse_lazy('dashboard:index')
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(generic.RedirectView):
    url = reverse_lazy('dashboard:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)

