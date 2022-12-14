from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path("bitstream/<int:id>/", bitstream, name='bitstream'),
]
