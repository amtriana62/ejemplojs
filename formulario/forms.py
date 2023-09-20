from django import forms

class CalculadoraForm(forms.Form):
    numero1 = forms.DecimalField(label='Número 1')
    numero2 = forms.DecimalField(label='Número 2')
    resultado = forms.DecimalField(label='Resultado', required=False)