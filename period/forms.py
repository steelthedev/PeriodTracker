from django import forms 

class PeriodForm(forms.Form):
  ovulation_cycle=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={
    'placeholder':'In form of 28',
    
  }))
  first_day_of_last=forms.CharField(required=True,widget=forms.TextInput(attrs={
    'placeholder':'In form of 2020-06-05',
    'class':'calendar'
  }))
  
  fields=[
    'first_day_of_last',
    ]
  