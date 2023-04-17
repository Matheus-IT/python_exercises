maior = 0
menor = 0
print('{:=^31}'.format('Peso pesado'))
for c in range(1, 5 + 1):
    peso = float(input('{}º Pessoa - Com licença, qual o seu peso? '.format(c)))
    # O primeiro peso vai ser o maior e o menor
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))
