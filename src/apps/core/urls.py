from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('home/', views.parking, name='home'),
    path('create/', views.create, name='create'),
]
