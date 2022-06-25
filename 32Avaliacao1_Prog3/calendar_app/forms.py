from cProfile import label
from django import forms


class CalendarForm(forms.Form):
    month = forms.IntegerField(label='Mês', min_value=1, max_value=12)
    year = forms.IntegerField(label='Ano', min_value=1)
