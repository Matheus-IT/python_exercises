op = ''
while op != 'N':
    print('{:=^36}'.format('Fatorial'))
    n = int(input('Você quer o fatorial de qual número? '))
    aux = n
    fat = 1

    print('\033[1;34m{}! = '.format(aux), end='')
    while aux > 0:
        #Quando 1, ele mostra =
        if aux == 1:
            print('{} = '.format(aux), end='')
        else:
            print('{} x '.format(aux), end='')
        fat *= aux #Cálculo do fatorial
        aux -= 1 #Decremento no contador
    print('{}\033[m'.format(fat))

    print()
    op = str(input('Mais um número [S/N]? ')).upper().strip()
    #Caso a opção esteja inválida
    while op != 'S' and op != 'N':
        print('\033[1;31mOpção inválida! Tente novamente!\033[m')
        op = str(input('Mais um número [S/N]? ')).upper().strip()
    print()
