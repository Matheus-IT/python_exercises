totDiv = 0
n = int(input('Digite um número: '))
for c in range(n, 0, -1):#Vai procurar de n até 1 quais são divisíveis por n
    if n % c == 0:
        totDiv += 1
        print('\033[1;31m{}\033[m'.format(c))
    else:
        print('\033[1;34m{}\033[m'.format(c))
if totDiv == 2:
    print('\033[1;35m{} é um número primo!\033[m'.format(n))
else:
    print('\033[1;32mO número {} não é primo!\033[m'.format(n))
