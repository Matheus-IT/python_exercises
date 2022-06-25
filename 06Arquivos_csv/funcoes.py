def lerInt(msg):
    while True:
        try:
            ent = int(input(msg))
        except:
            print('Entrada invalida', end='')
        else:
            break
    return ent


def lerStr(msg):
    while True:
        try:
            ent = str(input(msg)).strip().title()
        except:
            print('Entrada invalida', end='')
        else:
            break
    return ent


def mostra_menu():
    from os import system

    system('cls')
    print('='*35)
    print('Menu Opcoes'.center(35))
    print('='*35)


def opcoes():
    print(' [1]Mostrar lista \n [2]Cadastrar pessoa \n [3]Tirar pessoa \n [4]Sair')
    op = lerInt(' - Sua opcao: ')
    while op not in [1, 2, 3, 4]:
        op = lerInt(' - Fora das opções! Sua opcao: ')
    return op


def arquivo_criado(name):
    try:
        f = open(name, 'r')
        f.close()
    except:
        return False
    else:
        return True


def mostra_lista(name):
    with open(name, 'r') as f:
        for count, l in enumerate(f.readlines()):
            l = l.replace('\n', '') #Tirar quebra de linha
            l = l.split(',') #Separa linhas por vírgula
            print(f'N{count+1}: {l[0]:10}{l[1]:>5} Anos')
    return count #Retorna a quantidade de pessoas


def cadastrar_pessoa(name):
    n = lerStr(' - Digite seu nome: ')
    idade = lerInt(' - Digite sua idade: ')
    with open(name, 'a') as f:
        f.write(f'{n},{idade}\n') #Escreve na próxima linha


def tirar_pessoa(nome, qtd_pessoas):
    n = lerInt(' - Qual pessoa remover: ')
    while n not in range(qtd_pessoas):
        n = lerInt(' - Fora da lista! Qual pessoa remover: ')
    lista = {'nome':[], 'idade':[]}
    with open(nome, 'r') as f:
        #Passar os dados do arquivo para um dicionário:
        for l in f.readlines():
            l = l.split(',')
            lista['nome'].append(l[0])
            lista['idade'].append(l[1])
        #Remover o membro n-1 da lista de pessoas:
        del lista['nome'][n-1]
        del lista['idade'][n-1]
    with open(nome, 'w') as f:
        #Recolocar o resto do dicionário na lista:
        for c in range(len(lista['nome'])):
            f.write(f'{lista["nome"][c]},{lista["idade"][c]}')
