import funcoes
from os import system
from time import sleep


system('cls')
print(' - CALCULADORA 2.0 - ')
n1 = n2 = 0
n1 = funcoes.entra_com_valor(n1, '   Digite o primeiro valor: ')
n2 = funcoes.entra_com_valor(n2, '   Digite o segundo valor: ')
res = '' #Ele começa assim pra não aparecer no menu agora
operacao = ''
while True:
    op = 0
    system('cls')
    print(f' - MENU DE OPCOES - \n   [{n1}] {operacao} [{n2}]{res}\n   1 Soma \n   2 Subtracao \n   3 Multiplicacao \n   4 Divisao \n   5 Digitar outros valores \n   6 Sair')
    op = funcoes.entra_com_valor(op, ' -> Escolha uma opcao: ')
    if op == 1:
        res = f' - Resultado: {funcoes.soma(n1, n2)}'
        operacao = '+'
    elif op == 2:
        res = f' - Resultado: {funcoes.subtracao(n1, n2)}'
        operacao = '-'
    elif op == 3:
        res = f' - Resultado: {funcoes.multiplicacao(n1, n2)}'
        operacao = '*'
    elif op == 4:
        try:
            res = f' - Resultado: {funcoes.divisao(n1, n2):4.2f}'
        except (ValueError, ZeroDivisionError):
            res = funcoes.divisao(n1, n2)
        operacao = '/'
    elif op == 5:
        n1 = funcoes.entra_com_valor(n1, '   Digite o primeiro valor: ')
        n2 = funcoes.entra_com_valor(n2, '   Digite o segundo valor: ')
        res = '' #Ele começa assim pra não aparecer no menu agora
        operacao = ''
    elif op == 6:
        print(' - Saindo...')
        sleep(1)
        break
    else:
        res = ' - Não entendi'
        pass
