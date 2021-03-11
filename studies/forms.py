from django.db import models
from django.forms import ModelForm
from .models import *


class CreateStudieForm(ModelForm):
    class Meta:
        model = Studie
        fields = '__all__'
