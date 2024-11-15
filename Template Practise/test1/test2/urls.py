from django.contrib import admin
from django.urls import path
from . views import welcome,favorites

urlpatterns = [
    
    path('welcome/', welcome, name='welcome'),
    path('favorites/', favorites, name='favorites'),
]
