from django.urls import path
from .views import create_status

urlpatterns = [
    path('create_status/', create_status, name='create-status'),
]