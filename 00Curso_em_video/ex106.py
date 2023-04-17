from os import system
from time import sleep


def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', cor=4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~'*(tam+4))
    print(f'  {msg}')
    print('~'*(tam+4))
    print(c[0], end='')
    sleep(1)


#Programa principal
c = ('\033[m',       #0 -> sem cores 
     '\033[0;31m',   #1 -> cor vermelho
     '\033[0;32m',   #2 -> cor verde
     '\033[0;33m',   #3 -> cor amarelo
     '\033[0;34m',   #4 -> cor azul
     '\033[0;35m',   #5 -> cor roxo
     '\033[0;30m')   #6 -> cor branco
system('cls')
while True:    
    titulo('SISTEMA DE AJUDA PYHELP', cor=2)
    com = str(input(' - Funcao ou Biblioteca: '))
    if com.upper() == 'FIM':
        break
    else:
        ajuda(com)
titulo(' - Ate logo!!', cor=1)
