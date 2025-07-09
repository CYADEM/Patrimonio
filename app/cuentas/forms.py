# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'nombre', 'apellido', 'email', 'password1', 'password2', 'area']

from django import forms  # <-- Aquí está el import faltante
from .models import CustomUser

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'nombre', 'apellido', 'email', 'password', 'area']
        
        
# forms.py
from django import forms

class CrearColeccionForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la colección", max_length=100)
    campos = forms.CharField(label="Títulos de columna (separados por coma)", widget=forms.Textarea, help_text="Ejemplo: Nombre, Fecha, Descripción")
