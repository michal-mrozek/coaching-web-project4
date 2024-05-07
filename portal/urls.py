from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_with_me, name='work_with_me'),
    path('portal', views.portal, name='portal'),
]
