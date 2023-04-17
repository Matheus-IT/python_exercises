from math import hypot
'''
cop = float(input('Comprimento do cateto oposto: '))
cadj = float(input('Comprimento do cateto adjacente: '))
hip = (cop ** 2 + cadj ** 2) ** (1/2)
print('A hipotenusa mede: {:.2f}Cm'.format(hip))
'''

cop = float(input('\033[31mInforme o comprimento do cateto oposto Cm: \033[m'))
cadj = float(input('\033[32mInforme o comprimento do cateto adjacente Cm: \033[m'))
print('\033[33mO comprimento da hipotenusa é: {:.2f}Cm\033[m'.format(hypot(cop, cadj)))
