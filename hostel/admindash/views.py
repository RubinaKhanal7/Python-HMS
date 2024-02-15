from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from . models import *
from . forms import * 
from dashboard.models import BookRoom


# Create your views here.

class AdmindashHomeView(LoginRequiredMixin,TemplateView):
    template_name = "admindash/index.html"


#Room
class RoomListView(LoginRequiredMixin,ListView):
    template_name = "admindash/rooms/list.html"
    model = Room



class RoomCreateView(LoginRequiredMixin,CreateView):
    template_name = "admindash/rooms/form.html"
    form_class = RoomForm
    success_url = reverse_lazy('admindash:rooms-list')


class RoomUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "admindash/rooms/form.html"
    form_class = RoomForm
    model = Room
    success_url = reverse_lazy('admindash:rooms-list')

 
class RoomDetailView(LoginRequiredMixin,DetailView):
    template_name = "admindash/rooms/detail.html"
    model = Room


class RoomDeleteView(LoginRequiredMixin,DeleteView):
    model = Room
    success_url = reverse_lazy('admindash:rooms-list')

#BookRoom

class BookRoomListView(LoginRequiredMixin,ListView):
    queryset = BookRoom.objects.all()
    template_name = "admindash/bookrooms/list.html"
    model = BookRoom
    
class BookRoomCreateView(LoginRequiredMixin,CreateView):
    template_name = "admindash/bookrooms/form.html"
    form_class = BookRoomForm
    model = BookRoom
    success_url = reverse_lazy('admindash:bookrooms-list')

class BookRoomUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "admindash/bookrooms/form.html"
    form_class = BookRoomForm
    model = BookRoom
    success_url = reverse_lazy('admindash:bookrooms-list')


class BookRoomDetailView(LoginRequiredMixin,DetailView):
    template_name = "admindash/bookrooms/detail.html"
    model = BookRoom


class BookRoomDeleteView(LoginRequiredMixin,DeleteView):
    model = BookRoom
    success_url = reverse_lazy('admindash:bookrooms-list')
    