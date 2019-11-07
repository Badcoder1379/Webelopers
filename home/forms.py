from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')
    password1 = forms.CharField(max_length=30, required=True, help_text='Password1')
    password2 = forms.CharField(max_length=30, required=True, help_text='Password2')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean_username(self):
        data = self.cleaned_data['username']
        duplicate_users = User.objects.filter(username=data)
        if duplicate_users.exists():
            raise forms.ValidationError("نام کاربری شما در سیستم موجود است")
        return data

    def clean_password2(self):
        data = self.cleaned_data['password2']
        check = self.cleaned_data['password1']
        if data != check:
            raise forms.ValidationError("گذرواژه و تکرار گذرواژه یکسان نیستند")
        return data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
