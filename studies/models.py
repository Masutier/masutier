from django.db import models


class Studie(models.Model):
    STATUS = (
        ('University', 'University'),
        ('High School', 'High School'),
        ('Technical', 'Technical'),
        ('WorkShop', 'WorkShop'),
        ('Self', 'Self'),
        ('Other', 'Other'),
    )
    FINISH = (
        ('Yes', "Yes"),
        ('No', "No"),
        ('En Curso', "En Curso"),
    )
    kind = models.CharField(max_length=100, blank=True, null=True, choices=STATUS, default="Other")
    name = models.CharField(max_length=30, blank=False, null=False)
    remark = models.CharField(max_length=50, blank=True, null=True, default=" ")
    institution = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    monthStart = models.CharField(max_length=3, blank=True, null=True)
    yearStart = models.CharField(max_length=4, blank=True, null=True)
    monthEnd = models.CharField(max_length=3, blank=True, null=True)
    yearEnd = models.CharField(max_length=4, blank=False, null=False)
    finish = models.CharField(max_length=100, blank=True, null=True, choices=FINISH, default="Yes")

    def __str__(self):
        return self.name
