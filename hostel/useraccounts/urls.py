from django.urls import path
from . import views     

app_name= 'useraccounts'

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('', views.DashboardHomeView.as_view(), name='home'),
    path('logout', views.logoutUser, name='logout'),
]