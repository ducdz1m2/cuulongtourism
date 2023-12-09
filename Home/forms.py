from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email')
class CustomerForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'customer-username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'customer-email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'id': 'customer-password1'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'id': 'customer-password2'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match. Please enter the same password in both fields.")

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'login-username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'login-password'})