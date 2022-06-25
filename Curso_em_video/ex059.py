op = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('-='*15)
while op != 5:
    op = int(input('''Menu opções:
[1]Soma
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair
Qual sua opção? '''))
    print('-='*15)
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O {} é maior que {}!'.format(n1, n2))
        else:
            print('O {} é maior que {}!'.format(n2, n1))
    elif op == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('\033[1;31mOpção inválida! Tente novamente!\033[m')
    print()
print('Saiu!')
