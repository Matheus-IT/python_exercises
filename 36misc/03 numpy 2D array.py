import numpy as np
from random import randint


def preenche_matriz(m, lin, col): #Preencher a matriz
    for l in range(lin):
        for c in range(col):
            m[l].append(randint(1, 9))


def mostra_matriz(m, lin, col): #Mostrar a matriz
    for l in range(lin):
        for c in range(col):
            print(f'[{m[l][c]:^5}]', end=' ')
        print()


#Programa principal
mat = list()
matrizes = list()
for cont in range(2):
    mat.clear()
    i = int(input(f'Digite a quantidade de LINHAS da {cont+1}ª matriz: '))
    for c in range(i): #Adicionar as listas para linhas
        linha = []
        mat.append(linha)
    j = int(input(f'Digite a quantidade de COLUNAS {cont+1}ª da matriz: '))
    preenche_matriz(mat, i, j)
    print(f'{cont+1}º matriz: ')
    mostra_matriz(mat, i, j)
    matrizes.append(np.array(mat))
if matrizes[0].shape == matrizes[1].shape:
    print('A soma de mat1 + mat2 é igual a:')
    sMatriz = np.array(matrizes[0] + matrizes[1])
    mostra_matriz(sMatriz, sMatriz.shape[0], sMatriz.shape[1])
else:
    print('Só é possível somar matrizes de mesma ordem')
