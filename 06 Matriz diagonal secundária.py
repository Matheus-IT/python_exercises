from random import randint


def preenche_matriz(m, ord):
    lin = col = ord #Linhas, Colunas e Ordem
    for cont in range(lin): #Colocar a quantidade de linhas
        linha = []
        m.append(linha)
    for l in range(lin):
        for c in range(col):
            if l + c == ord - 1: #Diagonal secundária
                m[l].append(randint(1, 9))
            else:
                m[l].append(0)


def mostra_matriz(m, ord): #Mostrar a matriz
    lin = col = ord
    for l in range(0, lin):
        for c in range(0, col):
            if l + c == ord - 1:
                print(f'\033[1;33m|{m[l][c]:^3}|\033[m', end=' ')
            else:
                print(f'\033[1;34m|{m[l][c]:^3}|\033[m', end=' ')
        print()


#Programa principal
mat = list()
ordem = int(input('Digite a ordem da matriz: '))
preenche_matriz(mat, ordem)
mostra_matriz(mat, ordem)
