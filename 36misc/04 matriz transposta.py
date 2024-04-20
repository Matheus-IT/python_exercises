from random import randint
from time import sleep


def preenche_matriz(m, lin, col): #Preencher a matriz
    for l in range(lin):
        for c in range(col):
            m[l].append(randint(1, 9))


def mostra_matriz(m, lin, col):
    for l in range(lin):
        for c in range(col):
            print(f'|{m[l][c]}|', end=' ')
        print()


def matriz_transposta(m, lin, col): #Transpõe a matriz principal
    print()
    for c in range(0, col):
        for l in range(0, lin):
            sleep(1)
            print(f'\033[34m|{m[l][c]}|\033[m', end=' ')
        print()


#Programa principal
mat = list()
i = int(input('Quantas \033[34mLINHAS\033[m a matriz terá? '))
for cont in range(i): #Acrescenta a quantidade de linhas
    linha = []
    mat.append(linha)
j = int(input('Quantas \033[33mCOLUNAS\033[m a matriz terá? '))
preenche_matriz(mat, i, j)
mostra_matriz(mat, i, j)
matriz_transposta(mat, i, j)
