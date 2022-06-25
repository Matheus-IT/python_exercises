from os import system


def preencher(p):
    for cont in range(max):
        pessoas.append(str(input(f' - Digite o nome da {cont+1} pessoa: ')))


def procura(p):
    nome = str(input(' - Qual nome procurar: '))
    for cont in range(max):
        if p[cont] == nome:
            return ' - Achei! :)'
        elif cont == max-1:
            return ' - Nao achei! :('


#Programa principal
system('cls')
max = (5) #Maximo de pessoas
pessoas = list()
preencher(pessoas)
while True:
    print(procura(pessoas))
    resp = str(input(' - Procurar mais um [S/N]? ')).upper()[0]
    while (resp != 'S') and (resp != 'N'):
        resp = str(input(' - Opcao incorreta! Procurar mais um [S/N]? ')).upper()[0]
    if resp == 'N':
        break
print(' - Tchau! :)')
