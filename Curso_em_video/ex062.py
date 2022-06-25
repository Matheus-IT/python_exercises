n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da progressão: '))
termo10 = n1 + 10 * razao #O décimo termo
cont = 0 #Contador de termos
while n1 < termo10: #Mostra os dez primeiros termos
    print(n1, end=' ')
    n1 += razao
    cont += 1
op = 1
while op != 0:
    print()
    op = int(input('Quer ver mais quantos termos? '))
    termo10 += op * razao
    while n1 < termo10:
        print(n1, end=' ')
        n1 += razao
        cont += 1
print()
print('{:=^20}'.format('Finalizado'))
print('Foram exibidos {} termos'.format(cont))
