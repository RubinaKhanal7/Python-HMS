from django.shortcuts import render
from django.views.generic import FormView,View
from django.contrib.auth import login,logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import LoginForm

# Create your views here.
class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self,form):
        login(self.request, form.instance)
        return redirect(reverse_lazy('admindash:home'))


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(self.request)
        return redirect(reverse_lazy('accounts:login'))
