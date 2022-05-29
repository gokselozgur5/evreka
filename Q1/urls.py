from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lastpoint', views.lastpoint, name='last_point'),
]
