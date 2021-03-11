from django.urls import path, include
from .views import *

urlpatterns = [
    path('experiences', experiences, name="experiences"),
    path('createExperience', createExperience, name="createExperience"),
    path('editExperience/<int:pk>/', editExperience, name="editExperience"),
    path('deleteExperience/<int:pk>/', deleteExperience, name="deleteExperience"),
    
]
