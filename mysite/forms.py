from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'پدرام'})
                                 )
    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شریفی'})
                                )
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control', 'placeholder': 'example@user.com'})
                             )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control border-end-0', 'value': '12345678'
            , 'placeholder': 'رمز عبور خود را وارد کنید'}
            )
    )

    class Meta:
        model = User
        fields = ['email', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("ایمیل تکراری میباشد !")
        return email