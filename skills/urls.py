from django.urls import path, include
from .views import *

urlpatterns = [
    path('skills', skills, name="skills"),
    path('createSkill', createSkill, name="createSkill"),
    path('editSkill/<int:pk>/', editSkill, name="editSkill"),
    path('deleteSkill/<int:pk>/', deleteSkill, name="deleteSkill"),
]
