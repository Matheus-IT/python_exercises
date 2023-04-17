def area(l, c): #Função para calcular área
    a = l * c
    print(f'A área de um terreno {l:.1f} x {c:.1f} é de {a:.1f}m²')


print('Controle de terrenos')
print('-'*20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
