from os import system


def dados_jogador(n='<desconhecido>', g=0):
    return f' - O jogador {n} fez {g} gols no campeonato'


system('cls')
nome = str(input(' - Digite o nome do jogador: ')).strip().title()
gols = str(input(' - Digite quantos gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(dados_jogador(g=gols) if nome == '' else dados_jogador(nome, gols))
