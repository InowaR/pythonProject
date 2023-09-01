from django.urls import path
from .views import *

urlpatterns = [
    path('', index),  # http://localhost:8000/
    path('cats/', categories),  # http://localhost:8000/cats/
]
