s = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        s += c
print('''A soma dos número ÍMPARES que são MÚLTIPLOS
de 3 e que se encontram no intervalo de 
1 e 500 é igual a: {}'''.format(s))
