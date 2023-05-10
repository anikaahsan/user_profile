from django import forms 
from .models import Account

class AccountForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':''

    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={

    }))
   
    class Meta:
        model=Account
        fields=['first_name','last_name','email','password','confirm_password']
      

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].error_messages.update({'class':'list-unstyled text-danger'})
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

       
        
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data['password']
        confirm_password=cleaned_data['confirm_password']
        if password!=confirm_password:
            raise forms.ValidationError('"password" and "confirm password" does not match')
        
        if len(password)<=8:
            raise forms.ValidationError('password should contain atleast 8 characters')
        if password.isalnum():
            raise forms.ValidationError('password should contain at least one letter and one number')

        return self.cleaned_data 



   
      

# class SigninForm(forms.Form):

#     email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput())
    
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class']='form-control'
        