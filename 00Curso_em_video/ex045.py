from random import randint
from time import sleep
l = ['\033[32mPedra\033[m', '\033[30mPapel\033[m', '\033[37mTesoura\033[m']
op = int(input('''\033[33mSuas opções:\033[m
\033[1;32m[0]Pedra\033[m
\033[1;30m[1]Papel\033[m
\033[1;37m[2]Tesoura\033[m
\033[32mQual é a sua jogada?\033[m '''))
print('Stone!')
sleep(1)
print('Paper!')
sleep(1)
print('Scissors!!')
sleep(1.5)
computador = randint(0, 2)
print('Você jogou {} e o computador jogou {}'.format(l[op], l[computador]))

if (op == 0 and computador == 2) or (op == 1 and computador == 0) or (op == 2 and computador == 1):
    print('\033[1;34mVocê Ganhou!!\033[m')
elif op == computador:
    print('\033[1;30mVocês empataram')
else:
    print('\033[1;31mVocê Perdeu!\033[m')
