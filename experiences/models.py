from django.db import models


class Experience(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    institution = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)
    monthStart = models.CharField(max_length=3, blank=True)
    yearStart = models.CharField(max_length=4, blank=True)
    monthEnd = models.CharField(max_length=3, blank=True)
    yearEnd = models.CharField(max_length=5, blank=False, null=False)

    def __str__(self):
        return self.name
