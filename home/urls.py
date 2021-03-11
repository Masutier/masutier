from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('loginPage', loginPage, name="loginPage"),
    path('logoutUser', logoutUser, name="logoutUser"),
]
