valores = []
valores_pares = []
valores_impares = []
while True:
    valores.append(int(input('\nDigite um valor: ')))
    resp = str(input('Mais um valor? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for val in valores:
    if val % 2 == 0: #Se for um valor par
        valores_pares.append(val)
    elif val % 2 == 1: #Se for um valor ímpar
        valores_impares.append(val)
print('-='*15)
print('Valores    Pares    Impares: ')
for c in range(0, len(valores)):
    print(f'{valores[c]}',
          f'{valores_pares[c]:10}' if c < len(valores_pares) else '          ',
          f'{valores_impares[c]:9}' if c < len(valores_impares) else '         ')
print('-='*15)
