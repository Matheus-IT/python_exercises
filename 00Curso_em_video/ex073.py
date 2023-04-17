from time import sleep
brasileirao = ('Santos', 'Palmeiras', 'Flamengo', 'Atlético', 'São Paulo', 'Corinthians', 'Botafogo', 'Internacional', 'Ceará-SC', 'Bahia', 'Athletico-PR', 'Goiás', 'Grêmio', 'Vasco', 'Fortaleza', 'Fluminense', 'Cruzeiro', 'Chapecoense', 'CSA', 'Avaí')
cinco_primeiros = brasileirao[:5] #Guardar os cinco primeiros colocados
ultimos_4 = brasileirao[-4:] #Guardar os últimos quatro colocados
ordem_alf = sorted(brasileirao) #Armazenar a tabela em ordem alfabética
onde_chapecoense = brasileirao.index('Chapecoense') #Em que posição Chapecoense
while True:
    print('-'*40)
    print('{:=^40}'.format('Tabela Do Brasileirão'))
    print('-'*40)
    op = int(input('''
[1]Mostrar Tabela
[2]Os cinco primeiros colocados
[3]Os últimos 4 colocados
[4]Times em ordem alfabética
[5]Em que posição está a Chapecoense
[6]Sair do programa
=>> Escolher qual opção? '''))
    if op == 1:
        print('-'*40)
        for cont in brasileirao: #Mostrar a tabela completa
            print(cont)
        print('-'*40)
        sleep(4)
    elif op == 2:
        print('-'*40)
        for cont in cinco_primeiros: #Mostrar os cinco primeiros colocados
            print(cont)
        print('-'*40)
        sleep(4)
    elif op == 3:
        print('-'*40)
        for cont in ultimos_4: #Mostrar os últimos 4 colocados
            print(cont)
        print('-'*40)
        sleep(4)
    elif op == 4:
        print('-'*40)
        for cont in ordem_alf: #Mostrar os times em órdem alfabética
            print(cont)
        print('-'*40)
        sleep(4)
    elif op == 5:
        print(f'A Chapecoense está na {onde_chapecoense}ª posição') #Mostra onde está a chapecoense
    elif op == 6:
        break
print('Programa finalizado')
