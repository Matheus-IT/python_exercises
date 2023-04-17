from random import sample
from time import sleep
jogada = []
print('='*40)
print('{:^40}'.format('JOGO NA MEGA SENA'))
print('='*40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print() #Pular linha
print('{:=^40}'.format(f' SORTEANDO {jogos} JOGOS '))
for c in range(1, jogos + 1):
    jogada = sample(range(1, 60), k=6) #Coloca 6 números, possíveis de 1 a 60, sem repetições dentro da lista
    jogada.sort() #Organizar em ordem crescente
    print(f'Jogo {c}: \033[34m{jogada}\033[m')
    sleep(1)
    jogada.clear() #Após mostrar cada jogada, limpar a lista para a próxima
print('{:=^40}'.format(' BOA SORTE! '))
