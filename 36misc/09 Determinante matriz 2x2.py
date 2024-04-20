from os import system


def preenche_matriz(ord): #Preencher qualquer matriz quadrada
    for i in range(ord):
        mat.append([])
        for j in range(ord):
            mat[i].append(int(input(f'Digite o valor da posicao [{i},{j}]: ')))
    for i in range(ord):
        for j in range(ord):
            print(f'[{mat[i][j]:^3}]', end=' ')
        print()


def determinante_2x2(m, ord):
    diag_principal = 1
    diag_secundaria = 1
    if ord == 2:
        for i in range(ord):
            for j in range(ord):
                if i == j:
                    diag_principal *= mat[i][j]
                if i + j == ord - 1:
                    diag_secundaria *= mat[i][j]
        det = diag_principal - diag_secundaria
        return det
    else:
        return 'Ordem diferente de 2'


#PROGRAMA PRINCIPAL
system('cls')
mat = list()
ordem = int(input('Digite a ordem da matriz: '))
preenche_matriz(ordem)
determinante = determinante_2x2(mat, ordem)
if ordem == 2:
    print(f'O determinante da matriz 2x2 e igual a {determinante}')
else:
    print(determinante)
