from django import forms
from shiftrota.models import Shiftrotainfo

AVAILABLE_SHIFTS=[
    ('shift1','Morning'),
    ('shift2','General'),
    ('shift3','Afternoon'),
    ('shift4','Night'),
]

class HomeForm(forms.ModelForm):
    shift = forms.ChoiceField(label='shift',choices=AVAILABLE_SHIFTS)

    class Meta:
        model = Shiftrotainfo
        fields = ('first_name','shift','date') 