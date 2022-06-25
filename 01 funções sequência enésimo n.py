def enesimo(num):
    l = []
    for c in range(1, num+1):
        for i in range(c):
            l.append(c)
        print(l)
        l.clear()


def enesimo2(num):
    l = []
    for c in range(1, num+1):
        l.append(c)
        print(l)


#Programa principal
while True:
    print(f'{" Sequência N-ésimo Valor ":=^35}')
    n = int(input('Digite um número inteiro: '))
    op = int(input('''Qual tipo de contagem deseja fazer? 
[1º] Digite 1
[2º] Digite 2
=>> '''))
    while op != 1 and op != 2:
        op = int(input('\033[1;31mOpção incorreta!\033[mQual tipo de contagem deseja fazer? '))

    if op == 1:
        enesimo(n)
    elif op == 2:
        enesimo2(n)

    resp = str(input('Mais uma sequência? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('\033[1;31mOpção incorreta!\033[mMais uma sequência? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
