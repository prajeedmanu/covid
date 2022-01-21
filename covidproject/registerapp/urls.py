from . import views
from django.urls import path



urlpatterns = [
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('booking', views.booking, name='booking'),
    path('submit12', views.submit12, name='submit12'),
    path('exit', views.exit, name='exit'),
    path('blank', views.blank, name='blank'),
    ]