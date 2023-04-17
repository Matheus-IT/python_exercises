resp = 'S'
cont = 0 #Contador
s = 0 #Somatório de valores
while resp == 'S':
    cont += 1
    n = int(input('Digite o {}º número: '.format(cont)))
    s += n #Acumula soma dos valores

    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    else:
        menor = n

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    #Se a resposta for incorreta:
    while (resp != 'S') and (resp != 'N'):
        print()
        print('\033[1;31mResposta incorreta! Tente novamente\033[m')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    print()
    m = s/cont
print('-='*20)
print('''
Foram digitados {} valores
A Soma entre os valores é {}
A média entre eles é {:.2f}
O maior valor digitado foi {}
E o menor valor digitado foi {}
'''.format(cont, s, m, maior, menor))
