from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = 0
print('Os valores sorteados foram: ', end='') #Mostra os 5 valores sorteados
for c in range(0, 5):
    print(f'{numeros[c]} ', end='')
    #Qual o maior e menor número
    if c == 0:
        maior = menor = numeros[c]
    elif numeros[c] > maior:
        maior = numeros[c]
    elif numeros[c] < menor:
        menor = numeros[c]
print()
print(f'O maior número foi {maior}')
print(f'E o menor número foi {menor}')
