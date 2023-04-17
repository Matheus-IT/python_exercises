compras = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('='*40)
print('{:^40}'.format('Listagem de preços'))
print('='*40)
for cont in range(0, len(compras)):
    if cont % 2 == 0:
        print(f'{compras[cont]:.<31}', end='')
    else:
        print(f'R${compras[cont]:>7.2f}')
print('='*40)
