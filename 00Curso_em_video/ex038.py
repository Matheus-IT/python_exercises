n1 = int(input('\033[1;31mDigite o primeiro valor: \033[m'))
n2 = int(input('\033[1;33mDigite o segundo valor: \033[m'))
if n1 > n2:
    print('\033[1;34mO PRIMEIRO valor é maior!\033[m')
elif n2 > n1:
    print('\033[1;36mO SEGUNDO valor é maior!\033[m')
else:
    print('\033[1;35mO DOIS valores são iguais!\033[m')
