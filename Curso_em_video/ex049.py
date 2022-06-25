print('\033[1;35m{:=^40}\033[m'.format('Tabuada'))
n = float(input('\033[1;33mVocê quer ver a tabuada de qual número? \033[m'))
print('\033[32m-=\033[m'*20)
op = int(input('''\033[1;33mQual a tabuada que você quer ver?\033[m
\033[1;34m[1]Soma
[2]Subtração
[3]Multiplicação
[4]Divisão
=>> \033[m'''))
print('\033[32m-=\033[m'*20)
# Escolhe a opção da tabuada
if op == 1:
    for c in range(1, 11):
        print('\033[1;36m{} + {} = {:3.0f}\033[m'.format(n, c, n + c))
elif op == 2:
    for c in range(1, 11):
        print('\033[1;34m{} - {} = {:3.0f}\033[m'.format(n, c, n - c))
elif op == 3:
    for c in range(1, 11):
        print('\033[1;36m{} x {} = {:3.0f}\033[m'.format(n, c, n * c))
elif op == 4:
    for c in range(1, 11):
        print('\033[1;34m{} / {} = {:4.2f}\033[m'.format(n, c, n / c))
else:
    print('\033[1;31mOpção inválida, tente novamente\033[m')
