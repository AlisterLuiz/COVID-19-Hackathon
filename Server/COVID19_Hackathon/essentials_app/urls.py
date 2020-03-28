from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertData, name='home-page')
]


