'''
    PROG II - Terceira Avaliação -

    Integrantes:

    ADALINE NOGUEIRA FERNANDES FIRMO
    THIAGO VINICIOS LIMA DE ARAUJO SOUSA
    MATHEUS DA COSTA DA SILVA

    Questão 02
'''


import sys


class Taxi:
    def read(self, file=sys.stdin):
        data = file.readlines()
        for i in data:
            data_split = i.split()
            A, G, Ra, Rg = [float(x) for x in data_split]
            if A == G == Ra == Rg == 0.00:
                break
            elif (Ra / A) <= (Rg / G):
                print('G')
            else:
                print('A')


def main():
    taxi = Taxi()
    taxi.read()


if __name__ == '__main__':
    main()
