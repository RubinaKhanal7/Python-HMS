from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.views.generic import View
#from dashboard import all

from . models import *
from dashboard.views import DashboardHomeView 
from .forms import CreateUserForm
#create your views here

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' +user)
            return redirect(reverse_lazy('useraccounts:login'))


    context={'form':form}
    return render(request, 'useraccounts/register.html', context)


def loginPage(request):

    if request.method == 'POST':
       username= request.POST.get('username')
       password=request.POST.get('password')

       user = authenticate(request, username=username,password=password)

       if user is not None:
        login(request, user)
        return redirect(reverse_lazy('dashboard:home'))
       else:
            messages.info(request, 'Username or Password is incorrect')

      
    context={}
    return render(request, 'useraccounts/login.html', context)

def logoutUser(request):
        logout(request)  
        return redirect(reverse_lazy('useraccounts:login'))

    