import numpy as np


def preenche_matriz(*parametros):
    if len(parametros) == 2: #Matriz quadrada
        m = parametros[0]
        ordem = parametros[1]
        for l in range(ordem):
            m.append([])
            for c in range(ordem):
                m[l].append(float(input(f'Digite o valor para a posição [{l},{c}] ')))
        mostra_matriz(m, ordem)
    elif len(parametros) == 3: #Matriz retangular
        m = parametros[0]
        lin = parametros[1]
        col = parametros[2]
        for l in range(lin):
            m.append([])
            for c in range(col):
                m[l].append(float(input(f'Digite o valor para a posição [{l},{c}] ')))
        mostra_matriz(m, lin, col)


def mostra_matriz(*parametros):
    global lin, col, m
    if len(parametros) == 2: #Matriz quadrada
        m = parametros[0]
        ordem = parametros[1]
        for l in range(ordem):
            for c in range(ordem):
                print(f'|{m[l][c]:^3}|', end=' ')
            print()
    elif len(parametros) == 3: #Matriz retangular
        m = parametros[0]
        lin = parametros[1]
        col = parametros[2]
        for l in range(lin):
            for c in range(col):
                print(f'|{m[l][c]:^3}|', end=' ')
            print()


def multiplica_matriz(m1, m2):
    n_linA, n_colA = len(m1), len(m1[0])
    n_linB, n_colB = len(m2), len(m2[0])
    matC = list() #Matriz para o resultado

    m1np = np.array(m1)
    m2np = np.array(m2)
    if n_colA == n_linB:
        print('Resultado da multiplicação de \033[1;33mmatA\033[m com \033[1;34mmatB\033[m')
        for l in range(n_linA):
            matC.append([])
            for c in range(n_colB):
                matC[l].append(0)
                for k in range(n_colA):
                    matC[l][c] += m1np[l][k] * m2np[k][c]
        n_linC = n_linA
        n_colC = n_colB
        mostra_matriz(matC, n_linC, n_colC)
    else:
        print('\033[1;31mOperação não definida\033[m')


#Programa principal
matA = list()
matB = list()
matrizes = {'matrizA': '\033[1;33mMatA\033[m', 'matrizB': '\033[1;34mMatB\033[m'}
tipo = int(input(f'{matrizes["matrizA"]} será QUADRADA ou RETANGULAR? [1]QUADRADA [2]RETANGULAR '))
while tipo != 1 and tipo != 2:
    tipo = int(input(f'\033[1;31mOpção incorreta\033[m {matrizes["matrizA"]} será QUADRADA ou RETANGULAR? [1]QUADRADA [2]RETANGULAR '))

if tipo == 1: #MatrizA quadrada
    ordema = int(input(f'Qual a ordem da {matrizes["matrizA"]}? '))
    preenche_matriz(matA, ordema)
elif tipo == 2: #MatrizA retangular
    linA = int(input(f'Quantas LINHAS para {matrizes["matrizA"]}? '))
    colA = int(input(f'Quantas COLUNAS para {matrizes["matrizA"]}? '))
    preenche_matriz(matA, linA, colA)

tipo = int(input(f'{matrizes["matrizB"]} será QUADRADA ou RETANGULAR? [1]Quadrada [2]Retangular '))
while tipo != 1 and tipo != 2:
    tipo = int(input(f'\033[1;31mOpção incorreta\033[m {matrizes["matrizB"]} será QUADRADA ou RETANGULAR? [1]Quadrada [2]Retangular '))

if tipo == 1: #MatrizB quadrada
    ordemb = int(input(f'Qual a ordem da {matrizes["matrizB"]}? '))
    preenche_matriz(matB, ordemb)
elif tipo == 2: #MatrizB ratangular
    linB = int(input(f'Quantas LINHAS para {matrizes["matrizB"]}? '))
    colB = int(input(f'Quantas COLUNAS para {matrizes["matrizB"]}? '))
    preenche_matriz(matB, linB, colB)
multiplica_matriz(matA, matB)
