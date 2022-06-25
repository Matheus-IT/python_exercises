from django import forms


class FormPrime(forms.Form):
    number = forms.IntegerField(label='Número', min_value=0)
