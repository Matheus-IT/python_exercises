from random import randint
from time import sleep

print('\033[31m-=-\033[m'*20)
print('\033[30mVou pensar em um número entre 0 e 5. Tente adivinhar ;)\033[m')
print('\033[31m-=-\033[m'*20)
pensado = randint(0, 5)#Computador "pensando"
n = int(input('\033[1;33mEm qual número eu pensei? \033[m'))#Jogador tenta adivinhar
print('\033[1;34mProcessando...\033[m')
sleep(2)#Espera 2s
if n == pensado:
    print('\033[1;33mParabéns, você conseguiu me vencer!\033[m')
else:
    print('\033[1;33mGanhei! Eu pensei no número {} e não no {}!\033[m'.format(pensado, n))
