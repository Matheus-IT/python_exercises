jogadores = list()
tabela_jogador = dict()
partidas = list()

while True:
    tabela_jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    qtdPart = int(input(f'Quantas partidas {tabela_jogador["nome"]} jogou? '))

    for c in range(0, qtdPart): #Perguntar quantos gols para cada partida
        partidas.append(int(input(f' - Quantos gols na {c+1}º partida? ')))
    tabela_jogador['gols'] = partidas[:]
    tabela_jogador['total'] = sum(partidas)
    partidas.clear()

    jogadores.append(tabela_jogador.copy()) #Colocar o dicionário na lista de jogadores

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('\033[1;31mOpção incorreta!\033[m Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    print()

print('-='*20)
print('Nº  Nome       Gols           Total')
print('-='*20)
for c, j in enumerate(jogadores):
    print(f'{c+1:<1} - {j["nome"]:10} {str(j["gols"]):<14} {j["total"]:^5}')
while True:
    print('-='*20)
    op = int(input('Mostrar os dados de qual jogador? (999 parar) '))
    while op not in range(len(jogadores)+1) and op != 999:
        op = int(input('\033[1;31mOpção incorreta\033[m Mostrar os dados de qual jogador? (999 parar) '))
    if op == 999:
        break
    print('-'*20)
    print(f'Levantamento do jogador {jogadores[op-1]["nome"]}:')
    for k, v in enumerate(jogadores[op-1]['gols']):
        print(f' - No {k+1}º jogo ele fez {v} gols')

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('\033[1;31mOpção incorreta!\033[m Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
