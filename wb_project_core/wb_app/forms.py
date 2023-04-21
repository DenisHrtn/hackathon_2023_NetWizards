from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Логин'}),
                               error_messages={'invalid': 'Неверный логин'}, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
                               error_messages={'invalid': 'Неверный пароль'}, label='Пароль')
