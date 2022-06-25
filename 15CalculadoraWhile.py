from time import sleep
from os import system #Biblioteca para limpar a tela
import emoji


def cabecalho():
    system('cls') or None #Limpar tela
    print('='*40)
    print('{:=^40}'.format(' PROGRAMA CALCULADORA '))
    print('='*40)


def operacoes(n1, n2):
    print(f'   [{n1}] - [{n2}]')
    sleep(0.5)
    print(f' - Soma: {n1 + n2}')
    sleep(0.5)
    print(f' - Subtracao: {n1 - n2}')
    sleep(0.5)
    print(f' - Multiplicacao: {n1 * n2}')
    sleep(0.5)
    print(f' - Divisao: {n1 / n2:4.2f}') if (n2 != 0) else print(f' - Divisao Indeterminada')


#PROGRAMA PRINCIPAL
while True:
    cabecalho()
    v1 = float(input(' - Digite o primeiro valor: '))
    v2 = float(input(' - Digite o segundo valor: '))

    cabecalho()
    operacoes(v1, v2)

    #SAINDO DO PROGRAMA
    resp = str(input(' = Digitar outros valores? [S/N] ')).upper().strip()[0]
    while (resp not in 'SN'):
        resp = str(input(' - Opcao incorreta! Digitar outros valores? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        print(emoji.emojize(' - Tchau! :grimacing:', use_aliases=True))
        break
