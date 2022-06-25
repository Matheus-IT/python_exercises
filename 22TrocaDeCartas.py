from os import system


def ler_qtd(n, msg):
    n = int(input(msg))
    while (n < 1) or (n > 10000):
        n = int(input(f' - Entrada invalida!{msg}'))
    return n


def preencher_set_cartas(cartas, qtd, p):
    """ set de cartas, qtd de cartas, p de pessoa """
    from time import sleep

    print() #Pular linha
    for cont in range(qtd):
        carta = int(input(f' - Digite a {cont+1} carta de {p}: '))
        while (carta < 1) or (carta > 100000):
            carta = int(input(f' - \033[1;31mEntrada invalida!\033[m Digite a {cont+1} carta de {p}: '))
        cartas.append(carta)
    print(' - OK!')
    sleep(1) #Espera 1s


def retirar_repetidos(lista):
    l = list()
    for cont in range(len(lista)):
        if lista[cont] not in l:
            l.append(lista[cont])
    return l


def qtd_trocas(cartasA, cartasB):
    inter_a = list()
    inter_b = list()
    for i in range(len(cartasA)):
        for j in range(len(cartasB)):
            if cartasA[i] == cartasB[j]:
                break
            elif (j == len(cartasB)-1):
                inter_a.append(cartasA[i])
    inter_a = retirar_repetidos(inter_a) #Pego o conjunto interseccao de a e tiro os repetidos
    for i in range(len(cartasB)):
        for j in range(len(cartasA)):
            if cartasB[i] == cartasA[j]:
                break
            elif (j == len(cartasA)-1):
                inter_b.append(cartasB[i])
    inter_b = retirar_repetidos(inter_b) #Pego o conjunto interseccao de b e tiro os repetidos
    menor = inter_a if len(inter_a) < len(inter_b) else inter_b
    return len(menor)
                


#Programa principal
qa = 0
a = list() #Set cartas Alice
qb = 0
b = list() #Set cartas Beatriz
system('cls')
print('{:=^50}'.format(' TROCA DE CARTAS POKEMON '))
qa = ler_qtd(qa, ' Quantas cartas Alice possui? ')
qb = ler_qtd(qb, ' Quantas cartas Beatriz possui? ')
preencher_set_cartas(a, qa, 'Alice')
preencher_set_cartas(b, qb, 'Beatriz')
print(sorted(a))
print(sorted(b))
maximo_trocas = qtd_trocas(a, b)
print(f' - Maximo de trocas e igual a {maximo_trocas}')
