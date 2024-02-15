
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from useraccounts.models import Login
from . models import *
from . forms import * 
from admindash.models import Room


# Create your views here.

class DashboardHomeView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/index.html"

class DashboardHome1View(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/contact.html"

class DashboardHome2View(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/about.html"



#BookRoom
class BookRoomListView(LoginRequiredMixin,ListView):
    template_name = "dashboard/bookrooms/list.html"
    #queryset = Login.objects.filter(user=request.user)
    model = BookRoom
    def get_queryset(self):
        query = BookRoom.objects.all().filter(fullname=self.request.user)
        return query

class BookRoomList1View(LoginRequiredMixin,ListView):
    queryset = Room.objects.all()
    template_name = "dashboard/bookrooms/list1.html"
    model = BookRoom
    
class BookRoomCreateView(LoginRequiredMixin,CreateView):
    template_name = "dashboard/bookrooms/form.html"
    form_class = BookRoomForm
    model = BookRoom
    success_url = reverse_lazy('dashboard:bookrooms-list')

class BookRoomUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "dashboard/bookrooms/form.html"
    form_class = BookRoomForm
    model = BookRoom
    success_url = reverse_lazy('dashboard:bookrooms-list')


class BookRoomDetailView(LoginRequiredMixin,DetailView):
    template_name = "dashboard/bookrooms/detail.html"
    model = BookRoom


class BookRoomDeleteView(LoginRequiredMixin,DeleteView):
    model = BookRoom
    success_url = reverse_lazy('dashboard:bookrooms-list')
