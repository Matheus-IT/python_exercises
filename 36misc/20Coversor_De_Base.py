from os import system


def mostra_Res(r):
    for cont in range(0, len(r)):
        print(r[cont], end=' ')


def calc_binario(n): #Converter decimal para binario
    resto = list()
    nb = n
    c = 0
    while nb > 0: #Calcular quanto de espaco vai precisar
        resto.append(0)
        c += 1
        nb //= 2 #Divisao inteira
    nb = n
    while nb > 0:
        c -= 1
        resto[c] = nb % 2 #Armazenar resto da divisao
        nb //= 2
    return resto


def calc_octal(n): #Converter decimal para octal
    resto = list()
    nb = n
    c = 0
    while nb > 0: #Calcular quanto de espaco vai precisar
        resto.append(0)
        c += 1
        nb //= 8 #Divisao inteira
    nb = n
    while nb > 0:
        c -= 1
        resto[c] = nb % 8 #Armazenar resto da divisao
        nb //= 8
    return resto


def calc_exa(n): #Converter decimal para exadecimal
    resto = list()
    nb = n
    c = 0
    while nb > 0: #Calcular quanto de espaco vai precisar
        resto.append(0)
        c += 1
        nb //= 16 #Divisao inteira
    nb = n
    while nb > 0:
        c -= 1
        resto[c] = 'A' if nb % 16 == 10 else\
                   'B' if nb % 16 == 11 else\
                   'C' if nb % 16 == 12 else\
                   'D' if nb % 16 == 13 else\
                   'E' if nb % 16 == 14 else\
                   'F' if nb % 16 == 15 else nb % 16 #Armazenar resto da divisao
        nb //= 16
    return resto


#Programa principal
bin = list()
oct = list()
exa = list()
system('cls')
num = int(input(' - Digite um numero: '))
bin = calc_binario(num)
print(f' - {num} convertido em binario e:')
mostra_Res(bin)
oct = calc_octal(num)
print(f'\n - {num} convertido em octal e:')
mostra_Res(oct)
exa = calc_exa(num)
print(f'\n - {num} convertido em exadecimal e:')
mostra_Res(exa)
