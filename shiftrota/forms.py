from django import forms
from shiftrota.models import Shiftrotainfo
from bootstrap_datepicker_plus import DatePickerInput

AVAILABLE_SHIFTS=[
    ('shift1','Morning'),
    ('shift2','General'),
    ('shift3','Afternoon'),
    ('shift4','Night'),
]

class HomeForm(forms.ModelForm):
    Shift = forms.ChoiceField(label='Shift',choices=AVAILABLE_SHIFTS)
    #Date = forms.DateField(widget = widgets.AdminDateWidget)

    class Meta:
        model = Shiftrotainfo
        fields = ('Name','Shift','Date') 
        widgets = {
            'Date': DatePickerInput(format='%d/%m/%Y'), # default date-format %m/%d/%Y will be used
        }