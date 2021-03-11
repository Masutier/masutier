from django.db import models
from django.forms import ModelForm
from .models import *


class CreateExperiencesForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
