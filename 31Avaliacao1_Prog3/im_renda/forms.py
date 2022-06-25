from django import forms


class FormPessoa(forms.Form):
    nome = forms.CharField(max_length=50)
    renda = forms.DecimalField(
        label='Renda anual', min_value=0, decimal_places=2
    )
    dependentes = forms.IntegerField(min_value=0)
