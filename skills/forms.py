from django.db import models
from django.forms import ModelForm
from .models import *


class CreateSkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
