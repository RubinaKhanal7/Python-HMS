from django.urls import path
from . import views         


app_name= 'admindash'
 
urlpatterns = [  

     path('', views.AdmindashHomeView.as_view(), name='home'),
     path('index.html', views.AdmindashHomeView.as_view()),

     #Room
     path('rooms', views.RoomListView.as_view(), name='rooms-list'),
     path('rooms/create', views.RoomCreateView.as_view(), name='rooms-create'),
     path('rooms/<int:pk>/update', views.RoomUpdateView.as_view(), name='rooms-update'),
     path('rooms/<int:pk>/detail', views.RoomDetailView.as_view(), name='rooms-detail'),
     path('rooms/<int:pk>/delete', views.RoomDeleteView.as_view(), name='rooms-delete'),

     #BookRooms 
     path('bookrooms/list', views.BookRoomListView.as_view(), name='bookrooms-list'),
     path('bookrooms/create', views.BookRoomCreateView.as_view(), name='bookrooms-create'),
     path('bookrooms/<int:pk>/update', views.BookRoomUpdateView.as_view(), name='bookrooms-update'),
     path('bookrooms/<int:pk>/detail', views.BookRoomDetailView.as_view(), name='bookrooms-detail'),
     path('bookrooms/<int:pk>/delete', views.BookRoomDeleteView.as_view(), name='bookrooms-delete'),
]