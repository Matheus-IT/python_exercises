pares = 0
valores = (int(input(f'Digite um valor: ')),
           int(input(f'Digite um valor: ')),
           int(input(f'Digite um valor: ')),
           int(input(f'Digite um valor: ')))
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('Não foi digitado nenhum valor 3')
print('Os valores pares digitados: ', end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
