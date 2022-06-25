def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    if n1 == 0:
        r = 'Operacao invalida'
    else:
        r = float(n1) / float(n2)
    return r
