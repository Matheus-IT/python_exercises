tabela_jogador = dict()
partidas = list()

tabela_jogador['nome'] = str(input('Nome do jogador: ')).title().strip() #Nome do jogador
qtdPart = int(input(f'Quantas partidas {tabela_jogador["nome"]} jogou? ')) #Quantas partidas fulano jogou

for c in range(0, qtdPart): #Perguntar quantos gols para cada partida
    partidas.append(int(input(f' - Quantos gols na {c+1}º partida? '))) #Colocar na lista
tabela_jogador['gols'] = partidas[:]
tabela_jogador['total'] = sum(partidas) #A soma dos gols
print('-='*15)
print(tabela_jogador)
print('-='*15)
for k, v in tabela_jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*15)
print(f'O jogador {tabela_jogador["nome"]} jogou {qtdPart} partidas')
for c, v in enumerate(partidas):
    print(f' - Na partida {c+1}, fez {v} gols')
print(f'Totalizando {tabela_jogador["total"]} gols')
