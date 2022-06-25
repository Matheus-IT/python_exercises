n1 = int(input('\033[1;31mDigite o primeiro valor: \033[m'))
maior = n1
menor = n1
n2 = int(input('\033[1;35mDigite o segundo valor: \033[m'))
if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2
n3 = int(input('\033[1;36mDigite o terceiro valor: \033[m'))
if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3
print()
print('\033[1;37mO maior valor digitado foi {}\033[m'.format(maior))
print('\033[1;32mO menor valor digitado foi {}\033[m'.format(menor))
