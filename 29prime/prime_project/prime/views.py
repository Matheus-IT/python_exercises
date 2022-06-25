from typing import List
from django.http import HttpRequest
from django.shortcuts import render

from .forms import FormPrime


def prime_factors(n: int):
    '''Guarda fatores divisíveis por um número incremental'''
    factors: List[tuple] = list()

    f = 2

    while n > 1:
        if n % f == 0:
            factors.append((n, f))
            n //= f
        else:
            f += 1
    factors.append((1, None))
    return factors


def prime_index_view(request: HttpRequest):
    form = FormPrime(request.POST or None)

    if form.is_valid():
        factors = prime_factors(form.cleaned_data['number'])
        return render(request, 'prime/result.html', locals())

    return render(request, 'prime/index.html', locals())
