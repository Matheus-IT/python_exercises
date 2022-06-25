from random import randint
from time import sleep


def sorteia(l):
    print('Sorteando 5 valores: ', end='')
    sleep(1)
    for c in range(0, 5):
        l.append(randint(1, 10))
        print(l[c], end=' ')
        sleep(0.3)
    print('Pronto!')


def somaPar(l):
    sPar = 0
    for v in l:
        if v % 2 == 0: #Soma dos pares
            sPar += v
    sleep(1)
    print(f'Somando os valores pares de {l}, temos {sPar}')



#Programa principal
lista = list()
sorteia(lista) #Colocar 5 valores aleatórios
somaPar(lista) #Mostra a soma dos valores pares
