from django.urls import path
from . import views


app_name = 'authentication'

urlpatterns = [
    path('', views.authentication_starter, name='authentication_all')
]