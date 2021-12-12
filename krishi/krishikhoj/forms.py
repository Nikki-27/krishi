from django import forms
from django.db.models import fields
from .models import info

implements = [
    ('Harrow','Harrow'),
    ('Cultivator','Cultivator'),
    ('Rotavator','Rotavator'),
    ('Plough','Plough'),
    ('Paddy Thrasher','Paddy Thrasher'),
    ('Dumping Trailer','Dumping Trailer'),
    ('4 wheel Trailer','4 wheel Trailer')
]

class TForm(forms.ModelForm):
    implements = forms.MultipleChoiceField(label='Select all the implements you have', choices=implements, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = info
        fields = ['name','phone','city','state','zip','ntractor','implements']
        labels ={'name': 'Name','phone':'Phone Number','city':'City','state':'State','zip':'Zipcode','ntractor':'How many tractors do you own?'}

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'ntractor':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'zip':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            }