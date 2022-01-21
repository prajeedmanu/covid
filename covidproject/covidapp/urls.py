from . import views
from django.urls import path


app_name='covidapp'
urlpatterns = [
    path('',views.index,name='index'),
]
