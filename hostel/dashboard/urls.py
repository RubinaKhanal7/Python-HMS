from django.urls import path
from . import views         
  
app_name= 'dashboard'
 
urlpatterns = [  

     path('', views.DashboardHomeView.as_view() ,name='home'),
     path('index.html', views.DashboardHomeView.as_view()),
     path('contact.html', views.DashboardHome1View.as_view()),
     path('about.html', views.DashboardHome2View.as_view()),

     #BookRooms 
     path('bookrooms', views.BookRoomListView.as_view(), name='bookrooms-list'),
     path('bookrooms/list1', views.BookRoomList1View.as_view(), name='bookrooms-list1'),
     path('bookrooms/create', views.BookRoomCreateView.as_view(), name='bookrooms-create'),
     path('bookrooms/<int:pk>/update', views.BookRoomUpdateView.as_view(), name='bookrooms-update'),
     path('bookrooms/<int:pk>/detail', views.BookRoomDetailView.as_view(), name='bookrooms-detail'),
     path('bookrooms/<int:pk>/delete', views.BookRoomDeleteView.as_view(), name='bookrooms-delete'),
    

]