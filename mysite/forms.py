from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from mysite.models import Construccion
from .models import Animal
from .models import Pueblo, UbicacionEspecifica, UbicacionVariada
from .models import Enemigo
from .models import Planta
from .models import Arma
from .models import Consumible
from .models import Historia
from .models import Comentario
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8 \
           or not re.search(r'[A-Z]', password1) \
           or not re.search(r'[a-z]', password1) \
           or not re.search(r'\d', password1) \
           or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un símbolo."
            )
        return password1

      
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={
            'invalid': 'Introduce un correo electrónico válido.',
            'required': 'Este campo es obligatorio.'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        
class ConstruccionForm(forms.ModelForm):
    class Meta:
        model = Construccion
        fields = ['nombre', 'materiales', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'materiales': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


        from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'hostilidad', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'hostilidad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
        }





class PuebloForm(forms.ModelForm):
    class Meta:
        model = Pueblo
        fields = ['nombre', 'imagen', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class UbicacionEspecificaForm(forms.ModelForm):
    class Meta:
        model = UbicacionEspecifica
        fields = ['nombre', 'imagen', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class UbicacionVariadaForm(forms.ModelForm):
    class Meta:
        model = UbicacionVariada
        fields = ['nombre', 'imagen', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class EnemigoForm(forms.ModelForm):
    class Meta:
        model = Enemigo
        fields = ['nombre', 'tipo', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
        }






class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombre', 'tipo', 'descripcion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ArmaForm(forms.ModelForm):
    class Meta:
        model = Arma
        fields = ['numero', 'nombre', 'tipo', 'descripcion', 'imagen']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            }
        


class ConsumibleForm(forms.ModelForm):
    class Meta:
        model = Consumible
        fields = [
            'nombre', 'imagen',
            'hambre_normal', 'agua_normal', 'vida_normal', 'energia_normal',
            'hambre_dificil', 'agua_dificil', 'vida_dificil', 'energia_dificil'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'hambre_normal': forms.NumberInput(attrs={'class': 'form-control'}),
            'agua_normal': forms.NumberInput(attrs={'class': 'form-control'}),
            'vida_normal': forms.NumberInput(attrs={'class': 'form-control'}),
            'energia_normal': forms.NumberInput(attrs={'class': 'form-control'}),
            'hambre_dificil': forms.NumberInput(attrs={'class': 'form-control'}),
            'agua_dificil': forms.NumberInput(attrs={'class': 'form-control'}),
            'vida_dificil': forms.NumberInput(attrs={'class': 'form-control'}),
            'energia_dificil': forms.NumberInput(attrs={'class': 'form-control'}),
        }



class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = ['imagen', 'texto']
        widgets = {
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }




class EmailRecoveryForm(forms.Form):
        email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "tuemail@ejemplo.com"})
    )
        




        


class ComentarioForoForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu comentario...',
                'rows': 4
            }),
        }
        labels = {
            'contenido': ''
        }
