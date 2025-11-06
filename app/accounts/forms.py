from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Пароль ще раз", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def clean(self):
        c = super().clean()
        if c.get('password1') != c.get('password2'):
            raise forms.ValidationError("Паролі не співпадають")
        return c
