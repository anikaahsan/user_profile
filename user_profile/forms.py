from django import forms
from django_countries.data import COUNTRIES
from .models import Profile




class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(
        input_formats=['%d/%m/%Y '],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    class Meta:
        model=Profile
        fields=['image','country','gender','birthday','bio']
        widgets={
            
            'birthday':forms.DateInput(attrs={
                'class':'',
            }),
           'gender':forms.Select(attrs={
               'class':'',
           }),
           'country':forms.Select(attrs={
               'class':"",
           }),
           'bio':forms.Textarea(attrs={
               'class':"",
           }),
           'image':forms.FileInput(attrs={
               'class':'',
           })

        }