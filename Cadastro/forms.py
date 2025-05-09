from django import forms

from Cadastro.models import Cad_Passeios


class PasseiosForm(forms.ModelForm):
    class Meta:
        model = Cad_Passeios
        fields = '__all__'