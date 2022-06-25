from django.http import HttpRequest
from django.shortcuts import render

from . import forms
from .calendar import Calendar


def home_view(request: HttpRequest):
    form = forms.CalendarForm(request.GET or None)

    if form.is_valid():
        year = form.cleaned_data['year']
        month = form.cleaned_data['month']
        month_calendar = Calendar(locale='pt_BR.utf8').formatmonth(
            year, month, withyear=True
        )
        return render(request, 'calendar_app/result.html', locals())

    return render(request, 'calendar_app/home.html', locals())
