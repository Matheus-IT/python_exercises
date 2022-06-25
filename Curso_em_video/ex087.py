matriz = [[], [], []]
s_pares = maior_segunda_linha = s_terceira_coluna = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite o valor da posição [{i},{j}] ')))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')

        if matriz[i][j] % 2 == 0: #Acumular a soma dos valores pares
            s_pares += matriz[i][j]
        if j == 2: #Somar os valores da terceira coluna
            s_terceira_coluna += abs(matriz[i][j]) #Funciona com números negativos
        if i == 1: #O maior valor da segunda linha
            if j == 0 or matriz[i][j] > maior_segunda_linha:
                maior_segunda_linha = abs(matriz[i][j]) #Funciona com números negativos
    print() #Pular linha

print('-='*20)
print(f'A soma de todos os valores pares digitados foi de {s_pares}')
print(f'A soma dos valores da terceira coluna é {s_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')
print('-='*20)
