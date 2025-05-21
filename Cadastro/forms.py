from django import forms

from Cadastro.models import Cad_Passeios


class PasseiosForm(forms.ModelForm):
    class Meta:
        model = Cad_Passeios
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'destino': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destino do passeio'}),
            'localPartida': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Local de partida'}),
            'horarioPartida': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'}),
            'grupoWhats': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link do grupo do WhatsApp'}),
            'DataPasseio': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa', 'type': 'date'}),
        }