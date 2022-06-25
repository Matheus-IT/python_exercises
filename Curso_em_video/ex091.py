from random import randint
from time import sleep
from operator import itemgetter

print(f'{"Jogando o dado!":^25}')
print('-'*25)
game = {'\033[31mJogador1\033[m': randint(1, 6),
        '\033[34mJogador2\033[m': randint(1, 6),
        '\033[32mJogador3\033[m': randint(1, 6),
        '\033[35mJogador4\033[m': randint(1, 6)}

for k, v in game.items():
    print(f'O {k} tirou o nº {v}')
    sleep(1)

ranking = list() #Criar uma LISTA para salvar o ranking em ordem
ranking = sorted(game.items(), key=itemgetter(1), reverse=True) #Organizar ordem

print('-'*25)
print(f'{"Ranking:":^25}')
sleep(2)
for k, v in enumerate(ranking): #Ranking é uma lista
    print(f'{k+1}º lugar: {v[0]} com {v[1]} pontos')
print('-'*25)
