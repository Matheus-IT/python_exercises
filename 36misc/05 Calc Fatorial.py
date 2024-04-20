from time import sleep


def calc_fatorial(num):
    fat = 1 #Por causa da multiplicação
    for cont in range(num, 0, -1):
        fat *= cont #Calculo do fatorial
        sleep(1)
        print(cont, end=' x ' if cont > 1 else ' = ')
    print(fat)


n = int(input('Você quer o fatorial de qual número? '))
print(f'O fatorial de {n} é igual a : ', end='')
calc_fatorial(n)
