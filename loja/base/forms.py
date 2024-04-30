from django import forms
from django.contrib.auth.forms import UserCreationForm
from loja.base.models import User



class UserRegistrationForm(UserCreationForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    celular = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Celular'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'celular']
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'celular': 'Celular'
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("The passwords do not match.")
        return cleaned_data

