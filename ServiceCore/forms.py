from django import forms

class RegisterForm(forms.Form):
    firstName = forms.CharField(max_length=25)
    lastName = forms.CharField(max_length=25)
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)