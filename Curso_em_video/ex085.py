valores = [[], []]
v = 0
for c in range(1, 8):
    v = int(input(f'Digite o {c}º valor: '))
    if v % 2 == 0: #Valores pares
        valores[0].append(v)
    else: #Valores ímpares
        valores[1].append(v)
valores[0].sort() #Organiza os valores pares
valores[1].sort() #Organiza os valores ímpares

print('-='*15)
print(f'Lista de valores pares: {valores[0]}')
print(f'Lista de valores ímpares: {valores[1]}')
