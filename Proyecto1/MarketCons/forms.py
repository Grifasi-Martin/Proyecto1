from django import forms

class formSetCliente(forms.Form):
    usuario = forms.CharField(max_length=20)
    contra = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()