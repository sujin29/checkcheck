from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createHabbit/', views.createHabbit, name='createHabbit'),
    path('dashboard/', views.dashboard, name='dashboard')
]