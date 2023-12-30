from django import forms
from main.models import Cliente

class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'morada', 'contacto']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome e Apelido'}),
            'morada': forms.TextInput(attrs={'placeholder': 'Localidade'}),
            'contacto': forms.TextInput(attrs={'placeholder': 'Telemovel/Telefone'}),
        }