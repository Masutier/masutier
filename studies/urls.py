from django.urls import path, include
from .views import *

urlpatterns = [
    path('studies', studies, name="studies"),
    path('createStudie', createStudie, name="createStudie"),
    path('editStudie/<int:pk>/', editStudie, name="editStudie"),
    path('deleteStudie/<int:pk>/', deleteStudie, name="deleteStudie"),
]
