from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('viewer', view_all_messages)
]