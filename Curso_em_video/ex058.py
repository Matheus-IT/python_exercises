from time import sleep
from random import randint
print('\033[1;33m-=\033[m'*20)
print('\033[1;35mVou pensar em um número entre 0 e 10...\033[m')
print('\033[1;34mTente adivinhar :)\033[m')
print('\033[1;33m-=\033[m'*20)
n = randint(0, 10)#Computador pensando em um número
op = int(input('\033[1;32mQual número eu pensei? \033[m'))
tentativas = 1#Primeira tentativa
print('\033[1;36mProcessando...\033[m')
sleep(1)
while op != n:
    if op < n:
        print('\033[1;31mMAIS...Ainda não é esse...\033[m')
        op = int(input('\033[1;32mQual número eu pensei? \033[m'))
        tentativas += 1#Cada vez mais um nas tentativas
        print('\033[1;36mProcessando...\033[m')
        sleep(1)
    else:
        print('\033[1;31mMENOS...Ainda não é esse...\033[m')
        op = int(input('\033[1;32mQual número eu pensei? \033[m'))
        tentativas += 1  # Cada vez mais um nas tentativas
        print('\033[1;36mProcessando...\033[m')
        sleep(1)
print('\033[1;33m-=\033[m'*20)
print('\033[1;34mVocê acertou!!\033[m')
if tentativas == 1:
    print('\033[1;35mCaraca! Você conseguiu de primeira!\033[m')
elif tentativas <= 4:
    print('\033[1;36mVocê conseguiu com apenas {} tentativas\033[m'.format(tentativas))
elif tentativas >= 5:
    print('\033[1;32mVocê conseguiu, mas precisou de {} tentativas para ganhar...\033[m'.format(tentativas))
