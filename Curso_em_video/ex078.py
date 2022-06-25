valores = []
posicoes_maior = []
posicoes_menor = []
maior = menor = 0
for cont in range(0, 5): #Ler 5 valores e colocar dentro de "valores"
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

for c, val in enumerate(valores):
    if c == 0: #O primeiro valor será o maior e o menor
        maior = menor = val
    elif val > maior: #Atribuir o maior e o menor
        maior = val
    elif val < menor:
        menor = val

for c, val in enumerate(valores): #Colher as posições do maior e menor
    if val == maior:
        posicoes_maior.append(c)
    elif val == menor:
        posicoes_menor.append(c)

if len(posicoes_maior) > 1: #Se tiver mais de uma posição para mostrar
    print(f'O maior valor foi {maior} que está nas posições ', end='')
    for cont in range(0, len(posicoes_maior)):
        print(posicoes_maior[cont], end=', ' if cont < len(posicoes_maior) - 1 else '')
else:
    print(f'O maior valor foi {maior} que está na posição ', end='')
    for cont in posicoes_maior:
        print(cont, end=' ')

if len(posicoes_menor) > 1: #Se tiver mais de uma posição para mostrar
    print(f'\nO menor valor foi {menor} que está nas posições ', end='')
    for cont in range(0, len(posicoes_menor)):
        print(posicoes_menor[cont], end=', ' if cont < len(posicoes_menor) - 1 else '')
else:
    print(f'\nO menor valor foi {menor} que está na posição ', end='')
    for cont in posicoes_menor:
        print(cont, end=' ')
