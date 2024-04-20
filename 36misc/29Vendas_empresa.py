import numpy as np
from matplotlib import pyplot as plt


def mostrar(mes, nome_mes):
    print(f'Vendas mês de {nome_mes}')
    for c, v in enumerate(mes):
        print(f'Dia {c+1} - {v} mil')


def resumo(mes, nome_mes):
    x = list(range(30))
    plt.bar(x, mes, label=f'Mês de {nome_mes}')
    plt.legend()
    plt.title(f'Representação Vendas no Mês de {nome_mes}')
    plt.xlabel('Dias do mês')
    plt.ylabel('Vendas (mil)')
    plt.show()


def comparar(mes1, nome_mes1, mes2, nome_mes2):
    x = list(range(30))
    plt.plot(x, mes1, label=f'Mês de {nome_mes1}')
    plt.plot(x, mes2, label=f'Mês de {nome_mes2}')
    plt.legend()
    plt.title('Comparação dos dois meses')
    plt.xlabel('Dias do mês')
    plt.ylabel('Vendas (mil)')
    plt.show()


abril = np.array([45, 44, 43, 41, 38, 42, 39, 36, 35, 38, 39, 41, 43, 47, 49, 50, 48, 42, 46, 44, 42, 41, 46, 48, 47, 49, 59, 57, 55, 58])
maio = np.array([39, 41, 43, 47, 49, 50, 48, 42, 46, 44, 45, 44, 43, 41, 38, 42, 39, 36, 35, 38, 49, 50, 48, 42, 46, 44, 45, 44, 43, 41])
op = int(input(' - Mostrar status de qual mês? \n - [1] Abril \n - [2] Maio \n Opcao: '))
if op == 1:
    mostrar(abril, 'Abril')
    op = str(input(' - Ver resumo em gráfico? [S/N] ')).strip().upper()[0]
    if op == 'S':
        resumo(abril, 'Abril')
    op = str(input(' - Comparar com o mês de Maio? [S/N] ')).strip().upper()[0]
    if op == 'S':
        comparar(abril, 'Abril', maio, 'Maio')
elif op == 2:
    mostrar(maio, 'Maio')
    op = str(input(' - Ver resumo em gráfico? [S/N] ')).strip().upper()[0]
    if op == 'S':
        resumo(maio, 'Maio')
    op = str(input(' - Comparar com o mês de Maio? [S/N] ')).strip().upper()[0]
    if op == 'S':
        comparar(maio, 'Maio', abril, 'Abril')
