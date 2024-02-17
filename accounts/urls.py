from django.urls import path
from . import views

urlpatterns = [
    path('event-user/register/', views.EventUserRegisterView.as_view(), name='eventuser-register'),
    path('user/login/', views.EventUserLoginAPIView.as_view(), name='eventuser-login'),
    path('organizer/register/', views.OrganizerRegisterView.as_view(), name='organizer-register'),
    path('organizer/login/', views.OrganizerLoginAPIView.as_view(), name='organizer-login'),
    path('user/reset-password/', views.RequestEventUserPasswordResetEmail.as_view(), name='eventuser-reset-password'),
    path('organizer/reset-password/', views.RequestOrganizerPasswordResetEmail.as_view(), name='organizer-reset-password'),
    path('user/reset-password/confirm/<uidb64>/<token>/', views.EventUserPasswordTokenCheckAPI.as_view(), name='eventuser-reset-password-confirm'),
    path('organizer/reset-password/confirm/<uidb64>/<token>/', views.OrganizerPasswordTokenCheckAPI.as_view(), name='organizer-reset-password-confirm'),
    path('user/reset-password/complete/', views.SetNewEventUserPasswordAPIView.as_view(), name='eventuser-reset-password-complete'),
    path('organizer/reset-password/complete/', views.SetNewOrganizerPasswordAPIView.as_view(), name='organizer-reset-password-complete'),
    path('user/logout/', views.EventUserLogoutAPIView.as_view(), name='eventuser-logout'),
    path('organizer/logout/', views.OrganizerLogoutAPIView.as_view(), name='organizer-logout'),
    path('user/profile/', views.ProfileView.as_view(), name='eventuser-profile'),
]
