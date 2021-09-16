from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    adress = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'password'
        self.fields['confirm_password'].label = 'confirm_password'
        self.fields['phone'].label = 'phone'
        self.fields['first_name'].label = 'first_name'
        self.fields['last_name'].label = 'last_name'
        self.fields['email'].label = 'email'


    def clean_password(self):
        if self.self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise forms.ValidationError('пароли не совпадают')
        return self.cleaned_data

    def clean_email(self):
        if self.cleaned_data['email'].split('.')[-1] in ['org', 'net']:
            raise forms.ValidationError('Регистрация для домена {} невозможна'.format(self.cleaned_data['email'].split('.')[-1]))
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Пользователь с таким почтовым ящиком уже зарегистрирован')

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('Данный {} занят'.format(self.cleaned_data['username']))
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'phone', 'first_name', 'last_name', 'email']
