from django import forms
from django.core import validators
from first_app.models import Users,WebUsers
from django.contrib.auth.models import User


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify your email: ')
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(widget = forms.HiddenInput, required = False, validators=[validators.MaxLengthValidator(0)])
    
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        
        if email != verify_email:
            raise forms.ValidationError('Please Check the email fields!')
        
        
        
class UsersForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')  
        
        
        
class ProfileInfoForm(forms.ModelForm):
    
    class Meta():
        model = WebUsers
        
        fields =('portfolio','picture')
    
    
    
    
