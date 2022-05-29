from django.urls import path

from . import views

urlpatterns = [
    path('lastpoint', views.lastpoint, name='last_point'),
]
