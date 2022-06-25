n1 = int(input('\033[1;32mDigite um valor:\033[m '))
n2 = int(input('\033[1;31mDigite outro valor:\033[m '))
s = n1 + n2
print('\033[1;35mA soma entre {} e {} é igual a: {}\033[m'.format(n1, n2, s))
