n = int(input('\033[1;35mDigite um número: \033[m'))
print('\033[1;31mO dobro de {} é igual a {}\033[m'.format(n, (2 * n)))
print('\033[1;33mO triplo de {} é igual a {}\033[m'.format(n, (3 * n)))
print('\033[1;34mA raiz quadrada de {} é igual a {:.2f}\033[36m'.format(n, (n ** (1/2))))
