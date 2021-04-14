from django import forms 

class PeriodForm(forms.Form):
  ovulation_cycle=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={
    'placeholder':'In form of 28',
    
  }))
  first_day_of_last=forms.CharField(required=True,widget=forms.TextInput(attrs={
    'placeholder':'In form of 06-05-2024',
<<<<<<< HEAD
    'id':'picker'
=======

    'id':'picker'

>>>>>>> fe9aaf9f4e005ea7f8c24396ea02d39255381f47
    
  }))
  
  fields=[
    'first_day_of_last',
    ]
  