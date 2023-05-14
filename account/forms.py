from django import forms 
from .models import Account

# def password_validation(value):
       
        
#         print(len(value))
#         if len(value)<=8:
#             raise forms.ValidationError('password should contain atleast 8 characters')

class AccountForm(forms.ModelForm):
    password=forms.CharField(help_text=("password should contain 10 character with atleast 1 number"),widget=forms.PasswordInput(attrs={'class':''

    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={

    }))
   
    class Meta:
        model=Account
        fields=['first_name','last_name','email','password','confirm_password']
        # error_css_class='fw-bold text-danger'
        error_messages={}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].error_messages.update({'class':'list-unstyled text-danger'})
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
    
    # def clean_first_name(self):
    #     first_name=self.cleaned_data['first_name']
    #     if first_name.strip()=='':
    #         raise forms.ValidationError('This field cannot be null!!')
    
    # def clean_last_name(self):
    #     last_name=self.cleaned_data['last_name']
    #     if last_name.strip()=='':
    #         raise forms.ValidationError('This field cannot be null!!')
    
        
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data['password']
        confirm_password=cleaned_data['confirm_password']
        num=False
        
        if password!=confirm_password:
            raise forms.ValidationError('"password" and "confirm password" does not match')
        elif len(password) < 10:
            raise forms.ValidationError('password should contain atleast 8 characters')
        
        else:
            for character in password:
                if character.isdigit():
                    num=True
                    break
              
                    
            if num==False:        
                 raise forms.ValidationError('password should atleast contain 1 number ')
       
        return self.cleaned_data             
               
                   

       
    




   
      

        