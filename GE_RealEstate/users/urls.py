from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.log_in, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logoutUser, name='logout'),
]