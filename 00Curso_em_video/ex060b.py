op = ''
while op != 'N':
    print('{:=^36}'.format('Fatorial'))
    n = int(input('Ver fatorial do número: '))
    fat = 1 #Começa com 1 para a multiplicação funcionar

    print('\033[1;34m{}! = '.format(n), end='')
    for c in range(n, 0, -1):
        print('{} '.format(c), end='')
        print('x ' if c != 1 else '= ', end='') #Quando c == 1 mostre =
        fat *= c #Cálculo do fatorial
    print('{}\033[m'.format(fat))

    op = str(input('Mais um número [S/N]? ')).upper().strip()
    #Se a opção for inválida
    while op != 'S' and op != 'N':
        print('\033[1;31mOpção inválida! Tente novamente!\033[m')
        op = str(input('Mais um número [S/N]? ')).upper().strip()
    print()
