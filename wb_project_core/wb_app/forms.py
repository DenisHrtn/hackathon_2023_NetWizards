from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Product


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


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = ['title', 'description', 'photo', 'available', 'category', 'on_stock', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("Длина превышает 255 символов")

        return title

    def clean_context(self):
        content = self.cleaned_data['description']
        if len(content) > 300:
            raise ValidationError("Длина превышает 300 строк")
        return content