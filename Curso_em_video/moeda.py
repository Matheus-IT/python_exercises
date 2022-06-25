def moeda(p):
    return f'R${p:7.2f}'


def metade(p, f=True):
    if f:
        return moeda(p/2)
    return p / 2


def dobro(p, f=True):
    if f:
        return moeda(p*2)
    return p * 2


def aumentar(p, v, f=True):
    """p: preco; v: quanto porcento; f: formatacao"""
    if f:
        return moeda(((v/100) * p) + p)
    return p + ((v/100) * p)


def diminuir(p, v, f=True):
    """p: preco; v: quanto porcento; f: formatacao"""
    if f:
        return moeda(p - ((v/100) * p))
    return p - ((v/100) * p)


def resumo(p, a, r):
    """p: preco; a: aumento; r: reducao"""
    print(35*'=')
    print('RESUMO DO VALOR'.center(35))
    print(35*'=')
    print(f' - Preco analisado:\t{moeda(p)}')
    print(f' - Dobro do preco:\t{dobro(p, True)}')
    print(f' - Metade do preco:\t{metade(p, True)}')
    print(f' - {a}% de aumento:\t{aumentar(p, a, True)}')
    print(f' - {r}% de reducao:\t{diminuir(p, r, True)}')
    print(35*'-')
