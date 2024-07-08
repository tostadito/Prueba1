from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')
    username = forms.CharField(required=True, label='Nombre de usuario')
    password = forms.CharField(required=True, label='Contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
