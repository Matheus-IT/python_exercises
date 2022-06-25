def entra_com_valor(val=0, msg='Digite um valor: '):
    """val => Valor avaliar msg => mensagem exibir"""
    val = None
    while val == None:
        try:
            val = int(input(msg))
        except:
            print(' - Não entendi')
            pass
        else:
            return val


def soma(n1=0, n2=0):
    return n1 + n2


def subtracao(n1=0, n2=0):
    return n1 - n2


def multiplicacao(n1=0, n2=0):
    return n1 * n2


def divisao(n1=0, n2=0):
    res = 0
    try:
        res = n1 / n2
    except ZeroDivisionError:
        return ' - O denominador é 0, divisão inválida'
    else:
        return res
