from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from mysite.models import Construccion

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
      
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
class UserUpdateForm(forms.ModelForm):
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