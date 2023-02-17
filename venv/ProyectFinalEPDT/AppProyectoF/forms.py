from django import forms
from django.forms import ModelForm
from .models import Producto

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','precio','imagen']

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(help_text="Ingrese su correo de uso personal")
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput,help_text="Su contraseña no puede ser demasiado similar a su otra información personal, debe contener al menos 8 caracteres, no puede ser una contraseña de uso común y no puede ser completamente numérica")
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput,help_text="Ingrese la misma contraseña que antes, para verificación")

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']