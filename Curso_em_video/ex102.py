from time import sleep
from os import system


def fatorial(num, mostra):
    if mostra == 'S': #Com cálculo
        fat = 1  # Fazer com que a multiplicação funcione
        for c in range(num, 0, -1):
            fat *= c
            print(c, end=' x ' if c > 1 else ' = ')
            sleep(1)
        print(fat)
    else: #Sem cálculo
        fat = 1
        for c in range(num, 0, -1):
            fat *= c
        print(f'O fatorial de {num} é igual a {fat}')


#Programa Principal
system('cls')
print(f'{" Calcular Fatorial ":=^25}')
n = int(input('Digite um número do fatorial: '))
n = abs(n) #Considerar o valor absoluto
show = str(input('Mostrar o processo de cálculo do fatorial? [S/N] ')).upper().strip()[0]
while show not in 'SN':
    show = str(input('\033[1;31mOpção inválida!\033[mMostrar o processo de cálculo do fatorial? [S/N] ')).upper().strip()[0]
fatorial(n, show)
