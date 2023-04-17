from ex115.lib.interface import * #importar todos de 'interface'
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
        sleep(2)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        cabecalho(' NOVO CADASTRO ')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!!')
        break
    else:
        print('\033[1;31mERRO: Digite uma opção válida! \033[m')
        sleep(2)
arquivo = open('cursoemvideo.txt')
arquivo.close() #Fechando cursoemvideo.txt
