from django.db import models
from django.contrib.auth.models import User

AVAILABLE_SHIFTS=[
    ('shift1','Morning'),
    ('shift2','General'),
    ('shift3','Afternoon'),
    ('shift4','Night'),
]

class Shiftrotainfo(models.Model):
    first_name=models.CharField(max_length=50)
    shift = models.CharField(max_length=50,choices=AVAILABLE_SHIFTS)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return ('%s is in %s') %(self.first_name,self.shift)