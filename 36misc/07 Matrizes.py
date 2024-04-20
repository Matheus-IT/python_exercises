from random import randint
from time import sleep
from os import system


system('cls')
def mat_quadrada(m, ord):
    for cont in range(ord): #Quantidade de linhas
        m.append([])
    for l in range(ord):
        for c in range(ord):
            m[l].append(randint(-9, 9))
    mostra_matriz(mat, ordem)


def mat_linha(m, lin, col):
    m.append([])
    for l in range(lin):
        for c in range(col):
            m[l].append(randint(-9, 9))
    mostra_matriz(mat, linhas, colunas)


def mat_coluna(m, lin, col):
    for cont in range(lin):
        m.append([])
    for l in range(lin):
        for c in range(col):
            m[l].append(randint(-9, 9))
    mostra_matriz(mat, linhas, colunas)


def mat_nula(m, lin, col):
    for cont in range(lin):
        m.append([])
    for l in range(lin):
        for c in range(col):
            m[l].append(0)
    mostra_matriz(mat, linhas, colunas)


def mat_diagonal(m, ord):
    for cont in range(ord):
        m.append([])
    for l in range(ord):
        for c in range(ord):
            if l + c == ord - 1: #Diagonal secundária
                m[l].append(randint(1, 9))
            else:
                m[l].append(0)
    mostra_matriz(mat, ordem)


def mat_triangular(m, ord):
    for cont in range(ord):
        m.append([])
    sup_inf = int(input('Matriz triangular [1]Superior ou [2]Inferior? '))
    if sup_inf == 1:
        print('Triangular Superior')
        for l in range(ord):
            for c in range(ord):
                if l > c:
                    m[l].append(0)
                else:
                    m[l].append(randint(1, 9))
    elif sup_inf == 2:
        print('Triangular Inferior')
        for l in range(ord):
            for c in range(ord):
                if l < c:
                    m[l].append(0)
                else:
                    m[l].append(randint(1, 9))
    mostra_matriz(mat, ordem)


def mat_identidade(m, ord):
    for cont in range(ord):
        m.append([])
    for l in range(ord):
        for c in range(ord):
            if l == c:
                m[l].append(1)
            else:
                m[l].append(0)
    mostra_matriz(mat, ordem)


def mat_transposta(m, lin, col):
    for cont in range(lin):
        m.append([])
    #Preencher a matriz
    print('\nMatriz \033[1;34mA\033[m:')
    for l in range(lin):
        for c in range(col):
            m[l].append(randint(-9, 9))
            sleep(0.1)
            print(f'\033[1;34m|{m[l][c]:^3}|\033[m', end=' ')
        print()
    #Transpor matriz
    print('Matriz \033[1;32mA\'\033[m:')
    for c in range(col):
        for l in range(lin):
            sleep(0.1)
            print(f'\033[1;32m|{m[l][c]:^3}|\033[m', end=' ')
        print()


def mat_oposta(m, lin, col):
    for cont in range(lin):
        m.append([])
    #Preencher a matriz
    print('Matriz \033[1;34mA\033[m:')
    for l in range(lin):
        for c in range(col):
            m[l].append(randint(-9, 9))
            sleep(0.1)
            if m[l][c] > 0:
                print(f'\033[1;34m|{m[l][c]:^3}|\033[m', end=' ')
            else:
                print(f'\033[1;32m|{m[l][c]:^3}|\033[m', end=' ')
        print()
    print('Matriz \033[1;32m-A\033[m:')
    for l in range(lin):
        for c in range(col):
            m[l][c] = -m[l][c]
            sleep(0.1)
            if m[l][c] > 0:
                print(f'\033[1;34m|{m[l][c]:^3}|\033[m', end=' ')
            else:
                print(f'\033[1;32m|{m[l][c]:^3}|\033[m', end=' ')
        print()


def digite_sua_matriz(*parametros):
    if len(parametros) == 2: #Se for MATRIZ QUADRADA
        m = parametros[0]
        ord = parametros[1]
        for cont in range(ord):
            m.append([])
        for l in range(ord):
            for c in range(ord):
                m[l].append(int(input(f'Digite o elemento da posição [{l},{c}]: ')))
        mostra_matriz(mat, ordem)

    elif len(parametros) == 3: #Se for MATRIZ RETANGULAR
        m = parametros[0]
        lin = parametros[1]
        col = parametros[2]
        for cont in range(lin):
            m.append([])
        for l in range(lin):
            for c in range(col):
                m[l].append(int(input(f'Digite o elemento da posição [{l},{c}]: ')))
        mostra_matriz(mat, linhas, colunas)


def mostra_matriz(*parametros):
    global lin, col, m, ord
    if len(parametros) == 2: #Matriz quadrada
        m = parametros[0]
        ord = parametros[1]
        for l in range(ord):
            for c in range(ord):
                sleep(0.1)
                if m[l][c] == 0:
                    print(f'\033[1;32m|{m[l][c]:^3}|\033[m', end=' ')
                else:
                    print(f'\033[1;34m|{m[l][c]:^3}|\033[m', end=' ')
            print()
    elif len(parametros) == 3:#Matriz retângular
        m = parametros[0]
        lin = parametros[1]
        col = parametros[2]
        for l in range(lin):
            for c in range(col):
                sleep(0.1)
                if tipo == 2 or tipo == 3:
                    print(f'\033[1;36m|{m[l][c]:^3}|\033[m', end=' ')
                elif m[l][c] == 0:
                    print(f'\033[1;32m|{m[l][c]:^3}|\033[m', end=' ')
                else:
                    print(f'\033[1;34m|{m[l][c]:^3}|\033[m', end=' ')
            print()


#Programa principal
while True:
    mat = list()
    tipo = int(input(f'''\033[1;34m\n\n{"PROGRAMA TIPOS DE MATRIZES":=^44}\033[m
    \033[37m- [1]MATRIZ QUADRADA
    - [2]MATRIZ LINHA
    - [3]MATRIZ COLUNA
    - [4]MATRIZ NULA
    - [5]MATRIZ DIAGONAL SECUNDÁRIA
    - [6]MATRIZ TRIANGULAR
    - [7]MATRIZ IDENTIDADE
    - [8]MATRIZ TRANSPOSTA
    - [9]MATRIZ OPOSTA
    - [10]QUERO DIGITAR A MINHA
    - [11]SAIR\033[m
    Qual o tipo de matriz você quer ver? '''))
    system('cls')
    if tipo == 1:
        print('\nMATRIZ QUADRADA')
        ordem = int(input('Qual a ORDEM da matriz? '))
        mat_quadrada(mat, ordem)
    elif tipo == 2:
        print('\nMATRIZ LINHA')
        linhas = 1
        colunas = int(input('Quantas COLUNAS terá a matriz linha? '))
        mat_linha(mat, linhas, colunas)
    elif tipo == 3:
        print('\nMATRIZ COLUNA')
        linhas = int(input('Quantas LINHAS terá a matriz coluna? '))
        colunas = 1
        mat_coluna(mat, linhas, colunas)
    elif tipo == 4:
        print('\nMATRIZ NULA')
        linhas = int(input('Quantas LINHAS para a matriz nula? '))
        colunas = int(input('Quantas COLUNAS para a matriz nula? '))
        mat_nula(mat, linhas, colunas)
    elif tipo == 5:
        print('\nMATRIZ DIAGONAL SECUNDÁRIA')
        ordem = int(input('Qual a ordem da matriz diagonal secundária? '))
        mat_diagonal(mat, ordem)
    elif tipo == 6:
        print('\nMATRIZ TRIANGULAR')
        ordem = int(input('Qual a ordem da matriz triangular?'))
        mat_triangular(mat, ordem)
    elif tipo == 7:
        print('\nMATRIZ IDENTIDADE')
        ordem = int(input('Qual a ordem da matriz identidade? '))
        mat_identidade(mat, ordem)
    elif tipo == 8:
        print('\nTRANSPOR UMA MATRIZ')
        linhas = int(input('Quantas LINHAS da matriz a transpor? '))
        colunas = int(input('Quantas COLUNAS da matriz a transpor? '))
        mat_transposta(mat, linhas, colunas)
    elif tipo == 9:
        print('\nMATRIZ OPOSTA')
        linhas = int(input('Quantas linhas para a matriz oposta? '))
        colunas = int(input('Quantas colunas para a matriz oposta? '))
        mat_oposta(mat, linhas, colunas)
    elif tipo == 10:
        print('DIGITE SUA MATRIZ')
        q_ou_r = int(input('A matriz será quadrada ou retangular? [1]-Quadrada [2]-Retangular '))
        if q_ou_r == 1: #Matriz quadrada
            ordem = int(input('Digite a ordem da matriz: '))
            digite_sua_matriz(mat, ordem)
        elif q_ou_r == 2:#Matriz retangular
            linhas = int(input('Digite o número de LINHAS da matriz: '))
            colunas = int(input('Digite o número de COLUNAS da matriz: '))
            digite_sua_matriz(mat, linhas, colunas)
    elif tipo == 11:
        break
    else:
        print('\033[1;31mOpção inválida\033[m')
    sleep(2)
print('\033[1;33mSaindo...\033[m')
sleep(1)
