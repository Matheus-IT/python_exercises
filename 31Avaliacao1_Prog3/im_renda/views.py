from django.shortcuts import render

from im_renda.forms import FormPessoa


def imposto_renda(request):
    form = FormPessoa(request.POST or None)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        renda_anual = form.cleaned_data['renda']
        dependentes = form.cleaned_data['dependentes']
        renda_liquida = float(renda_anual) * (1.0 - 0.02 * int(dependentes))

        if 0.00 <= renda_liquida < 2000.00:
            imposto_recolher = 0
        elif 2000.00 <= renda_liquida < 5000.00:
            imposto_recolher = renda_liquida * 0.05
        elif 5000.00 <= renda_liquida < 10000.00:
            imposto_recolher = renda_liquida * 0.10
        else:
            imposto_recolher = renda_liquida * 0.15

        return render(
            request,
            'im_renda/result.html',
            context={
                'calc_result': {
                    'nome': nome,
                    'renda_anual': renda_anual,
                    'dependentes': dependentes,
                    'renda_liquida': renda_liquida,
                    'imposto_recolher': imposto_recolher,
                }
            },
        )

    return render(request, 'im_renda/home.html', context={'form': form})
