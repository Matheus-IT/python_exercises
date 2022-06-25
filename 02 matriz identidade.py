from os import system
mat = list()


def matriz_quadrada(): #Verificar se a matriz é quadrada
    if i == j:
        return True
    else:
        return False


def preenche_matriz(m): #Preencher a matriz
    if matriz_quadrada():
        for l in range(0, i):
            for c in range(0, j):
                if l == c:
                    m[l].append(1)
                else:
                    m[l].append(0)
    else:
        for l in range(0, i):
            for c in range(0, j):
                m[l].append(0)


def mostra_matriz(m): #Mostrar a matriz
    for l in range(0, i):
        for c in range(0, j):
            if matriz_quadrada():
                if l == c:
                    print(f'\033[1;33m[{m[l][c]:^3}]\033[m', end=' ')
                else:
                    print(f'\033[1;34m[{m[l][c]:^3}]\033[m', end=' ')
            else:
                print(f'\033[1;34m[{m[l][c]:^3}]\033[m', end=' ')
        print()


#Programa principal
system('cls')
i = int(input('Digite a quantidade de LINHAS da matriz: '))

for c in range(i): #Adiciona as linhas da matriz
    linha = []
    mat.append(linha)

j = int(input('Digite a quantidade de COLUNAS da matriz: '))
preenche_matriz(mat)
mostra_matriz(mat)
