#Parte inteira com trunc da biblioteca math
'''from math import trunc
n = float(input('Digite um número: '))
print('Valor inteiro: {}'.format(trunc(n)))'''

n = float(input('\033[36mDigite um valor: \033[m'))
print('\033[34mValor digitado foi {} e sua porção inteira é {}\033[m'.format(n, int(n)))
