from django.db import models

class Skill(models.Model):
    skill = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    dominium = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.name

