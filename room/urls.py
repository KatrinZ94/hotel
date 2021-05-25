from django.urls import path
from room import views


urlpatterns = [
    path('room_detail/<int:room_id>/', views.room_detail, name='room_detail'),
    path('room_like/<int:room_id>/', views.room_like, name='room_like'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.main_page, name='main_page'),
]
