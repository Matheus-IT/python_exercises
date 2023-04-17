valores = []
for c in range(0, 5):
    print(valores)
    v = int(input('Digite um valor: '))
    if c == 0 or v > valores[-1]:
        valores.append(v)
        print('Adicionado no final da lista!')
    else:
        for pos, val in enumerate(valores): #Varrer toda a lista
            if v <= valores[pos]: #Procurar a menor posição mais próxima para v
                valores.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista')
                break #Ponto de parada para sair do laço
    print()
print(f'\033[1;34mValores em ordem: {valores}\033[m')
