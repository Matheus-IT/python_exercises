sPares = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        sPares += n
        cont += 1
if cont <= 0:
    print('Você não digitou nenhum valor par')
else:
    print('\033[1;34mA soma dos {} valores pares é igual a {}\033[m'.format(cont, sPares))
