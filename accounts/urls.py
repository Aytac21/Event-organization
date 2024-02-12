from django.urls import path
from . import views

urlpatterns = [
    path('eventuser/register/', views.EventUserRegisterAPIView.as_view(), name='eventuser-register'),
    path('organizer/register/', views.OrganizerRegisterAPIView.as_view(), name='organizer-register'),
    path('eventuser/login/', views.EventUserLoginAPIView.as_view(), name='eventuser-login'),
    path('organizer/login/', views.OrganizerLoginAPIView.as_view(), name='organizer-login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='user-logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

]
