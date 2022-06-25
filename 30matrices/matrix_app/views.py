from django.shortcuts import render

from matrix_app.forms import FormMatrixDimension
from . import matrix_operations


def matrix_index_view(request):
    return render(request, 'matrix_app/index.html')


def matrix_operation_view(request, op: str):
    form = FormMatrixDimension(request.GET or None)

    if form.is_valid():
        lines = form.cleaned_data['lines']
        columns = form.cleaned_data['columns']

        result = matrix_operations.exec_operation(op, lines, columns)

        return render(request, 'matrix_app/result.html', locals())
    return render(request, 'matrix_app/operation.html', locals())
