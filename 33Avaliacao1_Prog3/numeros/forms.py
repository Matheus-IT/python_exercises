from django import forms


class FormNum(forms.Form):
    num = forms.IntegerField(label='Valor', min_value=1, max_value=100)
