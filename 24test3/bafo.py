'''
    PROG II - Terceira Avaliação -

    Integrantes:

    ADALINE NOGUEIRA FERNANDES FIRMO
    THIAGO VINICIOS LIMA DE ARAUJO SOUSA
    MATHEUS DA COSTA DA SILVA

    Questão 01
'''


class Jogador:
    def __init__(self):
        self.figurinhas = 0

    def adiciona_figurinhas(self, figs: int):
        self.figurinhas += figs


class Jurado:
    def __init__(self, jogador1: Jogador, jogador2: Jogador):
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def decidir_ganhador(self):
        if self.jogador1.figurinhas >= self.jogador2.figurinhas:
            return 'Aldo'
        else:
            return 'Beto'


partida = 0

while True:
    rodadas = int(input())

    if rodadas == 0:
        break

    partida = partida + 1

    aldo = Jogador()
    beto = Jogador()

    for i in range(rodadas):
        val1, val2 = list(map(int, input().split()))

        aldo.adiciona_figurinhas(val1)
        beto.adiciona_figurinhas(val2)

    print('Teste {}'.format(partida))

    j = Jurado(aldo, beto)
    ganhador = j.decidir_ganhador()
    print(ganhador + '\n')
