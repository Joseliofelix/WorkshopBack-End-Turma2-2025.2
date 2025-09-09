from django import forms

class ConsultaCepForm(forms.Form):
    cep = forms.CharField(label='CEP', max_length=9)
