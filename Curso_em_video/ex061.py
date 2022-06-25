print('{:=^36}'.format('Gerador de PA'))
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da progressão: '))
termo10 = n1 + 10 * razao
while n1 < termo10:
    print(n1, end=' ')
    n1 = n1 + razao
