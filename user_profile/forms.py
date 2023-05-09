from django import forms
from django_countries.data import COUNTRIES
from .models import Profile

#custom widget
class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(forms.ModelForm):
  
    
    class Meta:
        model=Profile
        fields=['image','country','gender','birthday','bio']
        widgets={
            
            'birthday':DateInput(attrs={
                'class':'form-control',
            }),
           'gender':forms.Select(attrs={
               'class':'form-control ',
           }),
           'country':forms.Select(attrs={
               'class':"form-control",
           }),
           'bio':forms.Textarea(attrs={
               'class':"form-control",
           }),
           'image':forms.FileInput(attrs={
               'class':'form-control',
           })

        }

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class']='form-control'
            