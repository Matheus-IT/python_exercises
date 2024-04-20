from time import sleep
from random import randint
from os import system


def preencher_lista(val, qtdade):
    for c in range(qtdade):
        val.append(int(input(f'Digite o valor da {c+1}ª posição : ')))


def organiza_lista(val):
    for n1 in range(len(val)):
        for n2 in range(len(val)):
            if val[n1] < val[n2]:
                val[n1], val[n2] = val[n2], val[n1] #Atribuição múltipla
    return val


#Programa principal
system('cls')
v = list()
qtd = int(input('Digite a quantidade de números a organizar: '))
preencher_lista(v, qtd)
print('Ordenando os valores...')
sleep(2)
print(organiza_lista(v))
