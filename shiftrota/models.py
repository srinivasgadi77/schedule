from django.db import models
from django.contrib.auth.models import User

AVAILABLE_SHIFTS=[
    ('shift1','Morning'),
    ('shift2','General'),
    ('shift3','Afternoon'),
    ('shift4','Night'),
]

class Shiftrotainfo(models.Model):
    Name=models.CharField(max_length=50)
    Shift = models.CharField(max_length=50,choices=AVAILABLE_SHIFTS)
    Date = models.DateField(blank=False)

    #whcih display the info on admin form
    def __str__(self):
        return ('%s is in %s on %s') %(self.Name,self.Shift,self.Date)