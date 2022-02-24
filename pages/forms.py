from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    credit_card = forms.CharField(
        label="信用卡號",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    birthday = forms.DateField(
        label="生日",
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'xxxx-xx-xx'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'credit_card', 'birthday', 'email', 'password1', 'password2')

    def clean_credit(self, *args, **kwargs):
        credit_card = self.cleaned_data.get("credit_card")
        if len(credit_card) != 16:
            raise forms.ValidationError("This is not a vaild credit_card")
        return credit_card