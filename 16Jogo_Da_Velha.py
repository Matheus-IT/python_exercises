from os import system
import emoji


def mostra_cabecalho():
    system('cls')
    print('=' * 30)
    print(f'{" JOGO DA VELHA ":=^30}')
    print('=' * 30)


def preenche_tab(mat):
    cont = 1
    for i in range(3):
        mat.append([])
        for j in range(3):
            mat[i].append(0)
            mat[i][j] = cont
            cont += 1


def mostra_tab(mat):
    for i in range(3):
        for j in range(3):
            print(f'[{mat[i][j]:^3}]', end=' ')
        print()


def verifica_tab(mat, jog):
    cont = 1
    for i in range(3):
        for j in range(3):
            if jog == cont:
                if (mat[i][j] != 'X') and (mat[i][j] != 'O'):
                    mat[i][j] = jogador
                else:
                    jog = int(input('\033[1;31mJa jogaram ai!\033[m Em qual casa jogar? '))
                    verifica_tab(mat, jog)
                    jog = 0 # -> Nao marcar numeros duas vezes
            cont += 1


def alguem_ganhou(mat):
    if (mat[0][0] == mat[1][1] == mat[2][2])\
            or (mat[0][2] == mat[1][1] == mat[2][0])\
            or (mat[0][0] == mat[0][1] == mat[0][2])\
            or (mat[1][0] == mat[1][1] == mat[1][2])\
            or (mat[2][0] == mat[2][1] == mat[2][2])\
            or (mat[0][0] == mat[1][0] == mat[2][0])\
            or (mat[0][1] == mat[1][1] == mat[2][1])\
            or (mat[0][2] == mat[1][2] == mat[2][2]):
        return True
    else:
        return False


def deu_velha(mat):
    simbolos = 0
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == 'O') or (mat[i][j] == 'X'):
                simbolos += 1
    if simbolos == 9: #Se todas as opcoes ja forem simbolos, deu velha
        return True
    else:
        return False


#PROGRAMA PRINCIPAL
global jogador, tab, jogada
tab = list() #Tabuleiro
jogador = '' #X ou O
jogada = 0 #Lugar da jogada

preenche_tab(tab)
while True:
    mostra_cabecalho()
    mostra_tab(tab)
    jogador = 'O' if jogador == 'X' else 'X' #Trocar jogador em cada jogada
    print(f' - Jogador {jogador}')
    jogada = int(input('Em qual casa jogar? '))
    while (jogada > 9) or (jogada < 1):
        jogada = int(input('\033[1;31mOpcao invalida!\033[m Em qual casa jogar? '))
    verifica_tab(tab, jogada)  #Marcar onde foi jogado
    if alguem_ganhou(tab):
        system('cls')
        mostra_cabecalho()
        ganhador = jogador
        print(f'\033[1;34mO jogador {ganhador} ganhou!\033[m')
        break
    if deu_velha(tab):
        system('cls')
        mostra_cabecalho()
        print(emoji.emojize('\033[1;31mDeu velha!\033[m :older_woman:', use_aliases=True))
        break
mostra_tab(tab)
