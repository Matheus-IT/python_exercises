import funcoes


n1 = int(input(' - Digite o primeiro valor: '))
n2 = int(input(' - Digite o segundo valor: '))
op = int(input(' - MENU DE OPCOES - \n   1 Soma \n   2 Subtracao \n   3 Multiplicacao \n   4 Divisao \n -> Escolha uma opcao: '))
print(' - Resultado: ', end='')
if op == 1:
    print(funcoes.soma(n1, n2))
elif op == 2:
    print(funcoes.subtracao(n1, n2))
elif op == 3:
    print(funcoes.multiplicacao(n1, n2))
elif op == 4:
    print(funcoes.divisao(n1, n2))
