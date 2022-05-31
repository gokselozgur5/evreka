from django.urls import path

from . import views

urlpatterns = [
    path('cfrq', views.getCollectionFrequency, name='last_point'),
]
