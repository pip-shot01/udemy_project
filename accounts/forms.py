from django import forms
from django.forms import ModelForm
# from  . models import Account 

from django.contrib.auth.models import User
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Password','class': 'form-control',
        }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Password','class': 'form-control',
        }))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Password','class': 'form-control',
        }))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Password','class': 'form-control',
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password','class': 'form-control',
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm Password','class': 'form-control',
        }))
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        
    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     for fields in self.fields:
    #          self.fields[fields].widget.attrs['class'] = 'form-control'


# class PasswordChangeForm(PasswordChangeForm):
#     class Meta: 
#         model = User
#         # fields = 