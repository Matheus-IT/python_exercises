from cProfile import label
from django import forms


class FormMatrixDimension(forms.Form):
    lines = forms.IntegerField(label='Linhas', min_value=1, max_value=50)
    columns = forms.IntegerField(label='Colunas', min_value=1, max_value=50)
