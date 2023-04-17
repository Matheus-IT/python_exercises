import emoji
from random import randint
print('-=-'*20)
print(emoji.emojize('Vamos jogar par ou impar? :smiley:', use_aliases=True))
print('-=-'*20)
venceu = 0
while True:
    op = int(input('Vai jogar quanto? '))
    par_impar = str(input('Você quer PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    while par_impar not in 'PI':#Se a opção não for nem Par nem Ímpar
        par_impar = str(input('\033[1;31mOpção inválida!\033[m Você quer PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]

    comp = randint(1, 10) #Computador vai escolher um número (1 a 10)
    soma = comp + op
    print()
    print('-=-'*20)
    print(f'Você jogou {op} e o computador jogou {comp}, total de {soma}. ', end='')
    if soma % 2 == 0: #Verificar se deu impar ou par
        print('\033[1;34mDeu PAR!!\033[m')
    else:
        print('\033[1;36mDeu ÍMPAR!!\033[m')

    if (par_impar == 'P' and soma % 2 == 0) or (par_impar == 'I' and soma % 2 == 1): #Se o usuário acertar o resultado
        print(f'\033[1;33mVocê ganhou!!!\033[m')
        venceu += 1
        print('\033[1;35mVamos jogar novamente!\033[m')
    else:
        print('\033[1;31mVocê perdeu\033[m')

        break
    print('- -'*20)
print(f'Game Over! Você venceu {venceu} vez(es)!')
