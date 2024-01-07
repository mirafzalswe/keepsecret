from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login-page'),
    path('logout/', views.LogoutView.as_view(), name='logout-page'),
    path('register/', views.registration_view, name='register-page'),
    path('profile/', views.ProfileUser.as_view(), name='profile-page'),
    path('profile/update/', views.EditProfileView.as_view(), name='profile-update')
]
